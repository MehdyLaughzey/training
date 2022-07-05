from pygame import midi





midi.init()





if midi.get_init():
    

    for deviceid in range (0,midi.get_count()-1):
        device=midi.get_device_info(deviceid)
        print("device detected (" + str(deviceid) +")\n"  + str(device))
        if device[2]==1:
            print("type:Input")
            
        elif device[3]==1:
            print("Type:output")
        if device[4]==1:
            print("port is open")
        print("--------------------------------")

    print ("default output id:" + str(midi.get_default_output_id()))
    print ("default input id:" + str(midi.get_default_input_id()))
        
    # # print(pygame.midi.get_default_input_id())
    # if midi.get_default_input_id()==-1:
    #     Print("No Input Device")
    # else:
    #     print("defualt Input device:\n" + str(midi.get_device_info(midi.get_default_input_id())))
    #     print(midi.get_default_input_id())
        
    # if midi.get_default_output_id()==-1:
    #     print("No output Device")
    # else:
    #     print("defualt output device:\n" + str(midi.get_device_info(midi.get_default_output_id())))
    #     print(midi.get_default_output_id())
    # midi.Input(midi.get_default_input_id())
# midi.
    # midi.Input(midi.get_default_input_id())
    # read=True
    # while read:
    #     midi.Input(midi.get_default_input_id(),4096)
    #     if midi.Input.poll(self):
    #         print(str(midi.Input.read(self, 4096)))

        
# print("defualt output device:\n" + str(midi.get_deInputvice_info(midi.get_default_output_id())))



midi.quit()