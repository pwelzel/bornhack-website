module Views.ScheduleOverview exposing (scheduleOverviewView)

-- Local modules

import Messages exposing (Msg(..))
import Models exposing (Model, Day, EventInstance, Filter)
import Views.FilterView exposing (filterSidebar, applyFilters, parseFilterFromQuery)


-- External modules

import Html exposing (Html, text, div, ul, li, span, i, h4, p, small, a)
import Html.Lazy exposing (lazy, lazy2)
import Html.Attributes exposing (class, classList, href, style)
import Date.Extra


scheduleOverviewView : Model -> Html Msg
scheduleOverviewView model =
    div [ class "row" ]
        [ filterSidebar model
        , div
            [ classList
                [ ( "col-sm-9", True )
                , ( "col-sm-pull-3", True )
                ]
            ]
            (List.map (\day -> lazy2 dayRowView day model) model.days)
        ]


dayRowView : Day -> Model -> Html Msg
dayRowView day model =
    let
        filteredEventInstances =
            applyFilters day model
    in
        div []
            [ h4 []
                [ text day.repr ]
            , div [ class "schedule-day-row" ]
                (List.map (lazy dayEventInstanceView) filteredEventInstances)
            ]


dayEventInstanceView : EventInstance -> Html Msg
dayEventInstanceView eventInstance =
    a
        [ classList
            [ ( "event", True )
            , ( "event-in-overview", True )
            ]
        , href ("#event/" ++ eventInstance.eventSlug)
        , style
            [ ( "background-color", eventInstance.backgroundColor )
            , ( "color", eventInstance.forgroundColor )
            ]
        ]
        ([ small []
            [ text
                ((Date.Extra.toFormattedString "HH:mm" eventInstance.from)
                    ++ " - "
                    ++ (Date.Extra.toFormattedString "HH:mm" eventInstance.to)
                )
            ]
         ]
            ++ (dayEventInstanceIcons eventInstance)
            ++ [ p
                    []
                    [ text eventInstance.title ]
               ]
        )


dayEventInstanceIcons : EventInstance -> List (Html Msg)
dayEventInstanceIcons eventInstance =
    let
        videoIcon =
            if eventInstance.videoUrl /= "" then
                [ i [ classList [ ( "fa", True ), ( "fa-film", True ), ( "pull-right", True ) ] ] [] ]
            else if eventInstance.videoRecording then
                [ i [ classList [ ( "fa", True ), ( "fa-video-camera", True ), ( "pull-right", True ) ] ] [] ]
            else
                []
    in
        [ i [ classList [ ( "fa", True ), ( "fa-" ++ eventInstance.locationIcon, True ), ( "pull-right", True ) ] ] []
        ]
            ++ videoIcon
