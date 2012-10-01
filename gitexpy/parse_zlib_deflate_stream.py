from . import zlibstream

def main(sys):
    do_profile = False
    if len(sys.argv) > 1 and sys.argv[1] == '--profile':
        do_profile = True
    if do_profile:
        import cProfile
        import pstats
        null = open('/dev/null', 'a')
        prof_file = 'profiler_output'
        cProfile.runctx(
            'zlibstream.parse(out_stream=null, info_stream=null)',
            locals(),
            globals(),
            filename=prof_file)
        stats = pstats.Stats(prof_file)
        stats.sort_stats('cumulative')
        stats.print_stats()
    else:
        zlibstream.parse()

if __name__ == '__main__':
    import sys
    main(sys)
