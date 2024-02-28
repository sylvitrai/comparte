def title(title: str):
    if osname == 'nt':
        """
        Changing the title in Windows' cmd
        is easy - just use the built-in
        title command
        """
        ossystem('title ' + title)
    else:
        """
        Most *nix terminals use
        this escape sequence to change
        the console window title
        """
        try:#use this later
            print('\33]0;' + title + '\a', end='')
            sys.stdout.flush()
        except Exception as e:
            print(e)
  with open(str(DATA_DIR) # save it on the new version folder
                            + '/Settings.cfg', 'w') as configfile:
                        configparser.write(configfile)
                    
                    pretty_print(Style.RESET_ALL + get_string('config_saved'), 
                                 "success", "sys0")
                except Exception as e:
                    pretty_print(f"Error saving configfile: {e}" + str(e), 
                                 "error", "sys0")
                    pretty_print("Config won't be carried to the next version",
                                 "warning", "sys0")
