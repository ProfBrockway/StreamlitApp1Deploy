# streamlit run "G:/My Drive/UConn/1-Subjects/Python/STAT476/CODE/StreamlitApp1Deploy/untitled0.py"

    # # ?V !!  Could try https://discuss.streamlit.io/t/streamlit-player/3169
    # # ?V This might fix the issue: https://github.com/streamlit/streamlit/issues/1580
    #                         also: https://discuss.streamlit.io/t/st-video-not-working-for-own-video-files-h264/5363  

    
# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import streamlit as st

# These are the formats supported in Streamlit right now.
VIDEO_EXTENSIONS = ["mp4", "ogv", "m4v", "webm"]

# For sample video files, try the Internet Archive, or download a few samples here:
# http://techslides.com/sample-webm-ogg-and-mp4-video-files-for-html5


st.title("Video Widget Examples")

st.header("Local video files")
st.write(
    "You can use st.video to play a locally-stored video by supplying it with a valid filesystem path."
)


def get_video_files_in_dir(directory):
    out = []
    for item in os.listdir(directory):
        try:
            name, ext = item.split(".")
        except:
            continue
        if name and ext:
            if ext in VIDEO_EXTENSIONS:
                out.append(item)
    return out


avdir = os.path.expanduser("~")
files = get_video_files_in_dir(avdir)


if len(files) == 0:
    st.write(
        "Put some video files in your home directory (%s) to activate this player."
        % avdir
    )

else:
    filename = st.selectbox(
        "Select a video file from your home directory (%s) to play" % avdir,
        files,
        0,
    )

    st.video(os.path.join(avdir, filename))
    
st.header("Remote video playback")
st.write("st.video allows a variety of HTML5 supported video links, including YouTube.")


def shorten_vid_option(opt):
    tempstr = opt.split("/")[-1]
    st.write ("CCCC" + opt)
    st.write ("DDDD" + tempstr)
    return (tempstr)


# A random sampling of videos found around the web.  We should replace
# these with those sourced from the streamlit community if possible!
vidurl = st.selectbox(
    label="Pick a video to play",
    options=(
        "https://youtu.be/_T8LGqJtuGc",
        "https://www.youtube.com/watch?v=kmfC-i9WgH0",
        "https://www.youtube.com/embed/sSn4e1lLVpA",
        "http://www.rochikahn.com/video/videos/zapatillas.mp4",
        "http://www.marmosetcare.com/video/in-the-wild/intro.webm",
        "https://www.orthopedicone.com/u/home-vid-4.mp4",
           ),
    index = 0,
    format_func =shorten_vid_option,
                        )
st.write("EEE" + vidurl)
st.video(vidurl)