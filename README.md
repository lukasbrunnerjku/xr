Install CMake... (https://cmake.org/download/) <br/>
Run the latest installer (e.g. cmake-3.20.0-windows-x86_64.msi) <br/>
Within the terminal navigate to the "flatbuffers" folder and execute: <br/>
git clone https://github.com/google/flatbuffers.git flatbuffers <br/>
Open CMake and specify the "flatbuffers" folder as source directory <br/>
Specify the "flatbuffers-build" as build directory, then Configure and Generate. <br/>
Open the project solution and build the solution (Release). <br/>
Next build the flatbuffers schemas with the flatc compiler. <br/>
Within the terminal navigate to the flatc.exe located at flatbuffers-build\Release and execute: <br/>
.\flatbuffers-build\Release\flatc.exe --python -o pose pose\schemas\req.fbs pose\schemas\rep.fbs