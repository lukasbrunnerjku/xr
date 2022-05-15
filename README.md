Having fun with Python and Unity.

https://openai.com/blog/emergent-tool-use/

Folder structure: <br/>
xr / flatbuffers <br/>
xr / flatbuffer-build <br/>

Install CMake... (https://cmake.org/download/) <br/>
Run the latest installer (e.g. cmake-3.20.0-windows-x86_64.msi) <br/>
Within the terminal navigate to the "flatbuffers" folder and execute: <br/>
git clone https://github.com/google/flatbuffers.git flatbuffers <br/>
Open CMake and specify the "flatbuffers" folder as source directory <br/>
Specify the "flatbuffers-build" as build directory, then Configure and Generate. <br/>
Open the project solution and build the solution (Release). <br/>
Next build the flatbuffers schemas with the flatc compiler. <br/>
Within the terminal navigate to the flatc.exe located at flatbuffers-build\Release and execute: <br/>
.\flatbuffers-build\Release\flatc.exe --python -o pose pose\schemas\req.fbs pose\schemas\rep.fbs <br/>
.\flatbuffers-build\Release\flatc.exe --csharp -o unity\GridWorld\Assets\Scenes\Plugins pose\schemas\req.fbs pose\schemas\rep.fbs <br/>

<!-- Download .zip from https://github.com/zeromq/libzmq <br/>
In CMake specify xr/unity/libzmq as source and xr/unity/libzmq-build as build folder. <br/>
Configure, Gernerate, Open Project, switch mode to Release, and make project. <br/> -->

Visit https://zeromq.org/get-started/, select C#, pick the NetMQ library (follow the github link: https://github.com/zeromq/netmq). <br/>
Download the .zip project netmq and build a Release version. <br/>
Afterwards I copied the content of the folder xr\unity\netmq\src\NetMQ\bin\Release\net46 into xr\unity\GridWorld\Assets\Scenes\Plugins. <br/>
Unity automatically detects all the dlls and will try to compile the C# script again. <br/>
I have not found a way to gracefully force unity to recompile my script, but everytime a change happens to the Assests unity will update it. <br/>
So a new blank line in the script is sufficient to force unity to recompile it. <br/>

Install the .NET SDK for Windows: https://dotnet.microsoft.com/en-us/download <br/>
and https://docs.microsoft.com/en-us/troubleshoot/developer/dotnet/framework/general/developer-language-pack <br/>
follow: https://www.youtube.com/watch?v=1saf4ahn-ek and restart Windows to make autocompletion etc. work in VS Code <br/>

https://google.github.io/mediapipe/solutions/hands <br/>
https://google.github.io/mediapipe/solutions/pose.html <br/>

Faster development with https://docs.unity3d.com/Manual/ConfigurableEnterPlayMode.html <br/>

