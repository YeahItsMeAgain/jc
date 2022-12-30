"""jc - JSON Convert `lsblk` command output parser

Usage (cli):

    $ lsblk | jc --lsblk

or

    $ jc lsblk

Usage (module):

    import jc
    result = jc.parse('lsblk', lsblk_command_output)

Schema:

    [
      {
        "name":         string,
        "maj_min":      string,
        "rm":           boolean,
        "size":         string,
        "ro":           boolean,
        "type":         string,
        "mountpoint":   string,
        "kname":        string,
        "fstype":       string,
        "label":        string,
        "uuid":         string,
        "partlabel":    string,
        "partuuid":     string,
        "ra":           integer,
        "model":        string,
        "serial":       string,
        "state":        string,
        "owner":        string,
        "group":        string,
        "mode":         string,
        "alignment":    integer,
        "min_io":       integer,
        "opt_io":       integer,
        "phy_sec":      integer,
        "log_sec":      integer,
        "rota":         boolean,
        "sched":        string,
        "rq_size":      integer,
        "disc_aln":     integer,
        "disc_gran":    string,
        "disc_max":     string,
        "disc_zero":    boolean,
        "wsame":        string,
        "wwn":          string,
        "rand":         boolean,
        "pkname":       string,
        "hctl":         string,
        "tran":         string,
        "rev":          string,
        "vendor":       string
      }
    ]

Examples:

    $ lsblk | jc --lsblk -p
    [
      {
        "name": "sda",
        "maj_min": "8:0",
        "rm": false,
        "size": "20G",
        "ro": false,
        "type": "disk",
        "mountpoint": null
      },
      {
        "name": "sda1",
        "maj_min": "8:1",
        "rm": false,
        "size": "1G",
        "ro": false,
        "type": "part",
        "mountpoint": "/boot"
      },
      ...
    ]

    $ lsblk -o +KNAME,FSTYPE,LABEL,UUID,PARTLABEL,PARTUUID,RA,MODEL,SERIAL,\\
      STATE,OWNER,GROUP,MODE,ALIGNMENT,MIN-IO,OPT-IO,PHY-SEC,LOG-SEC,ROTA,\\
      SCHED,RQ-SIZE,DISC-ALN,DISC-GRAN,DISC-MAX,DISC-ZERO,WSAME,WWN,RAND,\\
      PKNAME,HCTL,TRAN,REV,VENDOR | jc --lsblk -p
    [
      {
        "name": "sda",
        "maj_min": "8:0",
        "rm": false,
        "size": "20G",
        "ro": false,
        "type": "disk",
        "mountpoint": null,
        "kname": "sda",
        "fstype": null,
        "label": null,
        "uuid": null,
        "partlabel": null,
        "partuuid": null,
        "ra": 4096,
        "model": "VMware Virtual S",
        "serial": null,
        "state": "running",
        "owner": "root",
        "group": "disk",
        "mode": "brw-rw----",
        "alignment": 0,
        "min_io": 512,
        "opt_io": 0,
        "phy_sec": 512,
        "log_sec": 512,
        "rota": true,
        "sched": "deadline",
        "rq_size": 128,
        "disc_aln": 0,
        "disc_gran": "0B",
        "disc_max": "0B",
        "disc_zero": false,
        "wsame": "32M",
        "wwn": null,
        "rand": true,
        "pkname": null,
        "hctl": "0:0:0:0",
        "tran": "spi",
        "rev": "1.0",
        "vendor": "VMware,"
      },
      {
        "name": "sda1",
        "maj_min": "8:1",
        "rm": false,
        "size": "1G",
        "ro": false,
        "type": "part",
        "mountpoint": "/boot",
        "kname": "sda1",
        "fstype": "xfs",
        "label": null,
        "uuid": "05d927bb-5875-49e3-ada1-7f46cb31c932",
        "partlabel": null,
        "partuuid": null,
        "ra": 4096,
        "model": null,
        "serial": null,
        "state": null,
        "owner": "root",
        "group": "disk",
        "mode": "brw-rw----",
        "alignment": 0,
        "min_io": 512,
        "opt_io": 0,
        "phy_sec": 512,
        "log_sec": 512,
        "rota": true,
        "sched": "deadline",
        "rq_size": 128,
        "disc_aln": 0,
        "disc_gran": "0B",
        "disc_max": "0B",
        "disc_zero": false,
        "wsame": "32M",
        "wwn": null,
        "rand": true,
        "pkname": "sda",
        "hctl": null,
        "tran": null,
        "rev": null,
        "vendor": null
      },
      ...
    ]

    $ lsblk -o +KNAME,FSTYPE,LABEL,UUID,PARTLABEL,PARTUUID,RA,MODEL,SERIAL,\\
      STATE,OWNER,GROUP,MODE,ALIGNMENT,MIN-IO,OPT-IO,PHY-SEC,LOG-SEC,ROTA,\\
      SCHED,RQ-SIZE,DISC-ALN,DISC-GRAN,DISC-MAX,DISC-ZERO,WSAME,WWN,RAND,\\
      PKNAME,HCTL,TRAN,REV,VENDOR | jc --lsblk -p -r
    [
      {
        "name": "sda",
        "maj_min": "8:0",
        "rm": "0",
        "size": "20G",
        "ro": "0",
        "type": "disk",
        "mountpoint": null,
        "kname": "sda",
        "fstype": null,
        "label": null,
        "uuid": null,
        "partlabel": null,
        "partuuid": null,
        "ra": "4096",
        "model": "VMware Virtual S",
        "serial": null,
        "state": "running",
        "owner": "root",
        "group": "disk",
        "mode": "brw-rw----",
        "alignment": "0",
        "min_io": "512",
        "opt_io": "0",
        "phy_sec": "512",
        "log_sec": "512",
        "rota": "1",
        "sched": "deadline",
        "rq_size": "128",
        "disc_aln": "0",
        "disc_gran": "0B",
        "disc_max": "0B",
        "disc_zero": "0",
        "wsame": "32M",
        "wwn": null,
        "rand": "1",
        "pkname": null,
        "hctl": "0:0:0:0",
        "tran": "spi",
        "rev": "1.0",
        "vendor": "VMware,"
      },
      {
        "name": "sda1",
        "maj_min": "8:1",
        "rm": "0",
        "size": "1G",
        "ro": "0",
        "type": "part",
        "mountpoint": "/boot",
        "kname": "sda1",
        "fstype": "xfs",
        "label": null,
        "uuid": "05d927bb-5875-49e3-ada1-7f46cb31c932",
        "partlabel": null,
        "partuuid": null,
        "ra": "4096",
        "model": null,
        "serial": null,
        "state": null,
        "owner": "root",
        "group": "disk",
        "mode": "brw-rw----",
        "alignment": "0",
        "min_io": "512",
        "opt_io": "0",
        "phy_sec": "512",
        "log_sec": "512",
        "rota": "1",
        "sched": "deadline",
        "rq_size": "128",
        "disc_aln": "0",
        "disc_gran": "0B",
        "disc_max": "0B",
        "disc_zero": "0",
        "wsame": "32M",
        "wwn": null,
        "rand": "1",
        "pkname": "sda",
        "hctl": null,
        "tran": null,
        "rev": null,
        "vendor": null
      },
      ...
    ]
"""
import jc.utils
import jc.parsers.universal


class info():
    """Provides parser metadata (version, author, etc.)"""
    version = '1.9'
    description = '`lsblk` command parser'
    author = 'Kelly Brazil'
    author_email = 'kellyjonbrazil@gmail.com'
    compatible = ['linux']
    magic_commands = ['lsblk']
    tags = ['command']


__version__ = info.version


def _process(proc_data):
    """
    Final processing to conform to the schema.

    Parameters:

        proc_data:   (List of Dictionaries) raw structured data to process

    Returns:

        List of Dictionaries. Structured data to conform to the schema.
    """
    bool_list = {'rm', 'ro', 'rota', 'disc_zero', 'rand'}

    int_list = {'ra', 'alignment', 'min_io', 'opt_io', 'phy_sec', 'log_sec',
                'rq_size', 'disc_aln'}

    for entry in proc_data:
        for key in entry:
            if key in bool_list:
                entry[key] = jc.utils.convert_to_bool(entry[key])

            if key in int_list:
                entry[key] = jc.utils.convert_to_int(entry[key])

    return proc_data


def parse(data, raw=False, quiet=False):
    """
    Main text parsing function

    Parameters:

        data:        (string)  text data to parse
        raw:         (boolean) unprocessed output if True
        quiet:       (boolean) suppress warning messages if True

    Returns:

        List of Dictionaries. Raw or processed structured data.
    """
    jc.utils.compatibility(__name__, info.compatible, quiet)
    jc.utils.input_type_check(data)

    # Clear any blank lines
    cleandata = list(filter(None, data.splitlines()))
    raw_output = []

    if jc.utils.has_data(data):

        cleandata = data.splitlines()

        cleandata[0] = cleandata[0].lower()
        cleandata[0] = cleandata[0].replace(':', '_')
        cleandata[0] = cleandata[0].replace('-', '_')

        raw_output = jc.parsers.universal.sparse_table_parse(cleandata)

        # clean up non-ascii characters, if any
        for entry in raw_output:
            entry['name'] = entry['name'].encode('ascii', errors='ignore').decode()

    if raw:
        return raw_output
    else:
        return _process(raw_output)
