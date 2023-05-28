from termcolor import colored
import random
import time

#this is a list of tuples containing the past tense, present participle, and past participle of tech action words.
process = [
    ('simulate', 'simulating', 'simulated'),
    ('load', 'loading', 'loaded'),
    ('calculate', 'calculating', 'calculated'),
    ('download', 'downloading', 'downloaded'),
    ('generate', 'generating', 'generated'),
    ('compile', 'compiling', 'compiled'),
    ('optimize', 'optimizing', 'optimized'),
    ('initialize', 'initializing', 'initialized'),
    ('encrypt', 'encrypting', 'encrypted'),
    ('decrypt', 'decrypting', 'decrypted'),
    ('render', 'rendering', 'rendered'),
    ('transcode', 'transcoding', 'transcoded'),
    ('compress', 'compressing', 'compressed'),
    ('decompress', 'decompressing', 'decompressed'),
    ('scan', 'scanning', 'scanned'),
    ('analyze', 'analyzing', 'analyzed'),
    ('verify', 'verifying', 'verified'),
    ('authenticate', 'authenticating', 'authenticated'),
    ('upload', 'uploading', 'uploaded'),
    ('parse', 'parsing', 'parsed'),
    ('extract', 'extracting', 'extracted'),
    ('validate', 'validating', 'validated'),
    ('sort', 'sorting', 'sorted'),
    ('filter', 'filtering', 'filtered'),
    ('cache', 'caching', 'cached'),
    ('stream', 'streaming', 'streamed'),
    ('index', 'indexing', 'indexed'),
    ('synchronize', 'synchronizing', 'synchronized'),
    ('convert', 'converting', 'converted'),
    ('archive', 'archiving', 'archived'),
    ('serialize', 'serializing', 'serialized'),
    ('deserialize', 'deserializing', 'deserialized'),
    ('sample', 'sampling', 'sampled'),
    ('normalize', 'normalizing', 'normalized'),
    ('aggregate', 'aggregating', 'aggregated'),
    ('embed', 'embedding', 'embedded'),
    ('preprocess', 'preprocessing', 'preprocessed'),
    ('interpolate', 'interpolating', 'interpolated'),
    ('extrapolate', 'extrapolating', 'extrapolated'),
    ('transform', 'transforming', 'transformed'),
    ('transpose', 'transposing', 'transposed'),
    ('smooth', 'smoothing', 'smoothed'),
    ('refactor', 'refactoring', 'refactored'),
    ('benchmark', 'benchmarking', 'benchmarked'),
    ('store', 'storing', 'stored'),
    ('retrieve', 'retrieving', 'retrieved'),
    ('query', 'querying', 'queried'),
    ('compact', 'compacting', 'compacted'),
    ('replicate', 'replicating', 'replicated'),
    ('shuffle', 'shuffling', 'shuffled'),
    ('broadcast', 'broadcasting', 'broadcasted'),
    ('resize', 'resizing', 'resized'),
    ('transmit', 'transmitting', 'transmitted'),
    ('monitor', 'monitoring', 'monitored'),
    ('schedule', 'scheduling', 'scheduled'),
    ('balance', 'balancing', 'balanced'),
    ('crawl', 'crawling', 'crawled'),
    ('record', 'recording', 'recorded'),
    ('merge', 'merging', 'merged'),
    ('split', 'splitting', 'split'),
    ('reconstruct', 'reconstructing', 'reconstructed'),
    ('evaluate', 'evaluating', 'evaluated'),
    ('learn', 'learning', 'learned'),
    ('predict', 'predicting', 'predicted'),
    ('infer', 'inferring', 'inferred'),
    ('train', 'training', 'trained'),
    ('retrain', 'retraining', 'retrained'),
    ('fine-tune', 'fine-tuning', 'fine-tuned'),
    ('test', 'testing', 'tested'),
    ('export', 'exporting', 'exported'),
    ('import', 'importing', 'imported'),
    ('deploy', 'deploying', 'deployed'),
    ('inspect', 'inspecting', 'inspected'),
    ('debug', 'debugging', 'debugged'),
    ('log', 'logging', 'logged'),
    ('track', 'tracking', 'tracked'),
    ('profile', 'profiling', 'profiled'),
    ('scale', 'scaling', 'scaled'),
    ('restart', 'restarting', 'restarted'),
    ('upgrade', 'upgrading', 'upgraded'),
    ('migrate', 'migrating', 'migrated'),
    ('configure', 'configuring', 'configured'),
    ('patch', 'patching', 'patched'),
    ('authorize', 'authorizing', 'authorized'),
    ('connect', 'connecting', 'connected'),
    ('disconnect', 'disconnecting', 'disconnected'),
    ('request', 'requesting', 'requested'),
    ('respond', 'responding', 'responded'),
    ('handle', 'handling', 'handled'),
    ('audit', 'auditing', 'audited'),
    ('sign', 'signing', 'signed'),
    ('invalidate', 'invalidating', 'invalidated'),
    ('route', 'routing', 'routed'),
    ('resolve', 'resolving', 'resolved'),
    ('load balance', 'load balancing', 'load balanced'),
    ('receive', 'receiving', 'received'),
    ('encode', 'encoding', 'encoded'),
    ('decode', 'decoding', 'decoded'),
    ('search', 'searching', 'searched'),
    ('match', 'matching', 'matched'),
    ('rank', 'ranking', 'ranked'),
    ('recommend', 'recommending', 'recommended'),
    ('visualize', 'visualizing', 'visualized'),
    ('retrieve', 'retrieving', 'retrieved')
]

#this is a list of tech things or nouns
things = [
    'geometry',
    'polygons',
    'network',
    'images',
    'data',
    'files',
    'documents',
    'videos',
    'audio',
    'text',
    'messages',
    'notifications',
    'settings',
    'configurations',
    'logs',
    'databases',
    'tables',
    'records',
    'charts',
    'graphs',
    'statistics',
    'metrics',
    'reports',
    'dashboards',
    'widgets',
    'modules',
    'components',
    'libraries',
    'plugins',
    'extensions',
    'packages',
    'dependencies',
    'models',
    'algorithms',
    'classifiers',
    'predictions',
    'recommendations',
    'labels',
    'features',
    'weights',
    'embeddings',
    'variables',
    'parameters',
    'hyperparameters',
    'gradients',
    'losses',
    'accuracies',
    'results',
    'errors',
    'exceptions',
    'warnings',
    'tasks',
    'jobs',
    'operations',
    'requests',
    'responses',
    'endpoints',
    'routes',
    'queries',
    'matches',
    'searches',
    'indexes',
    'caches',
    'sessions',
    'users',
    'clients',
    'customers',
    'visitors',
    'subscribers',
    'followers',
    'likes',
    'comments',
    'posts',
    'articles',
    'blogs',
    'forums',
    'threads',
    'categories',
    'tags',
    'products',
    'orders',
    'payments',
    'invoices',
    'shipments',
    'transactions',
    'accounts',
    'balances',
    'permissions',
    'roles',
    'organizations',
    'teams',
    'workspaces',
    'environments',
    'servers',
    'instances',
    'containers',
    'virtual machines',
    'clusters',
    'deployments',
    'services',
    'pipelines',
    'workflows',
    'events',
    'traces',
    'alarms',
    'backups',
    'archives',
    'preferences',
    'profiles',
    'tokens',
    'authentication',
    'authorizations',
    'credentials',
    'encryption',
    'keys',
    'certificates',
    'signatures',
    'buffers',
    'queues',
    'streams',
    'connections',
    'sockets',
    'packets',
    'content',
    'media',
    'metadata',
    'encodings',
    'formats',
    'structures',
    'representations',
    'schemas',
    'templates',
    'styles',
    'themes',
    'translations',
    'localizations',
    'interfaces',
    'frameworks',
    'utilities',
    'tools',
    'applications',
    'platforms',
    'systems',
    'devices',
    'browsers',
    'operating systems',
    'APIs',
    'SDKs'
]

#this list contains describing words that can be injected into the generated lines for flavor
descriptive = [
    'secure',
    'temporary',
    'volatile',
    'encrypted',
    'authenticated',
    'compressed',
    'optimized',
    'processed',
    'analyzed',
    'validated',
    'filtered',
    'cached',
    'decrypted',
    'streamlined',
    'indexed',
    'synchronized',
    'converted',
    'archived',
    'serialized',
    'deserialized',
    'normalized',
    'aggregated',
    'embedded',
    'preprocessed',
    'interpolated',
    'extrapolated',
    'transformed',
    'transposed',
    'smoothed',
    'benchmark',
    'stored',
    'retrieved',
    'queried',
    'compacted',
    'replicated',
    'shuffled',
    'broadcasted',
    'resized',
    'transmitted',
    'monitored',
    'scheduled',
    'balanced',
    'crawled',
    'recorded',
    'merged',
    'split',
    'sampled',
    'reconstructed',
    'evaluated',
    'learned',
    'predicted',
    'verified',
    'inferred',
    'trained',
    'retrained',
    'fine-tuned',
    'tested',
    'compiled',
    'exported',
    'imported',
    'deployed',
    'inspected',
    'debugged',
    'logged',
    'tracked',
    'profiled',
    'benchmarked',
    'scaled',
    'restarted',
    'upgraded',
    'migrated',
    'configured',
    'patched',
    'authorized',
    'connected',
    'disconnected',
    'requested',
    'responded',
    'handled',
    'audited',
    'signed',
    'invalidated',
    'routed',
    'resolved',
    'load balanced',
    'decompressed',
    'received',
    'encoded',
    'decoded',
    'searched',
    'matched',
    'sorted',
    'ranked',
    'recommended',
    'visualized',
    'calibrated',
    'executed',
    'categorized',
    'grouped',
    'summarized',
    'formatted',
    'parsed',
    'generated',
    'traced'
]

#this list contains some error text options.
errors = [
    'aborted',
    'failed',
    'quit unexpectedly',
    'exited'
]

#this is a list of potential names of paths on a file tree
directories = [
    'home',
    'system',
    'tmp',
    'bin',
    'lib',
    'data',
    'config',
    'var',
    'usr',
    'dev',
    'log',
    'proc',
    'media',
    'mnt',
    'opt',
    'run',
    'srv',
    'etc',
    'usr',
    'root',
    'sys',
    'srv',
    'app',
    'cache',
    'doc',
    'user',
    'kernel',
    'net',
    'pkg',
    'queue',
    'backup',
    'plugin'
]

root_dirs = [
    '~/',
    '/home/',
    '/root/',
    '/etc/',
    '/sys/',
    '/'
]

def get_error_text():
    # return a tuple containing a line of babble, and an error referencing the first line. 
    my_task = random.choice(process)
    my_target = ' ' + random.choice(things)
    text = colored(my_task[1].capitalize() + my_target + '...', 'green')
    secondary_text = ''

    rand = random.randint(1,3)
    if rand == 1:
        secondary_text = colored('WARNING:', 'red') + colored(' ' + my_task[1] + my_target + ' ' + random.choice(errors) + '.', 'grey')
    if rand == 2:
        secondary_text = colored('Failed to ' + str(my_task[0] + my_target + '.'),'red')
    if rand == 3:
        secondary_text = colored('!!! ', 'red') + colored("Couldn't " + str(my_task[0] + my_target + '. '),'grey') + colored('!!!', 'red')
    return (text, secondary_text)

def get_simple_text():
    # simply create a colored string combining the words in our lists. 
    return colored(random.choice(process)[1].capitalize() + ' ' + random.choice(things) + "...", "green")

def get_flavorful_text():
    # this is the same as get_simple_text, except it adds and extra descriptive word in the middle. 
    return colored(random.choice(process)[1].capitalize() + ' ' + random.choice(descriptive) + ' ' + random.choice(things) + "...", "green")

def get_speed_text():
    # return a 3 tuple containing a line of babble, and a followup line tracking the speed of the process.
    timer = round(random.random() * 100,2)
    unit = random.choice(['GB', 'Gb','KB','Kb','KiB', 'GiB','MB','Mb','MiB','bytes'])
    my_task = random.choice(process)
    my_target = random.choice(things)
    chance = random.randint(1,3)
    if chance == 1:
        text = colored(my_task[1].capitalize() + ' ' + my_target + '...', 'green')
        secondary_text = colored(my_task[1].capitalize() + ' at ' + str(timer) + unit + '/s.', 'grey')
        return(secondary_text,text)
    elif chance == 2:
        text = colored(my_task[1].capitalize() + ' ' + my_target + '...', 'green')
        secondary_text = colored(my_target.capitalize()  + ' used ' + str(timer) + unit + ' of additional disk space.', 'blue')
        return(text,secondary_text)    
    else:
        text = colored(my_task[1].capitalize() + ' ' + my_target + '...', 'green')
        secondary_text = colored(my_target.capitalize()  + ' used ' + str(timer) + unit + ' of memory.', 'grey')
        return(text,secondary_text)

def get_timed_text():
    # return a 3 tuple containing a line of babble, a followup line tracking the time that process took,
    # and that generated amount of time in milliseconds, for your optional use. 
    timer = random.randint(0,512)
    my_task = random.choice(process)
    my_target = random.choice(things)
    text = colored(my_task[1].capitalize() + ' ' + my_target + '...', 'green')
    secondary_text = colored(my_target.capitalize() + ' ' + my_task[2] + ' in ' + str(timer) + 'ms.', 'grey')
    return(text,secondary_text,timer)

def get_directory():
    length = random.randint(1,10)
    dir = random.choice(root_dirs)
    for i in range(0,length):
        dir = dir + random.choice(directories) + '/'
    return dir

def get_directory_text():
    chance = random.randint(1,3)
    if chance == 1:
        return colored('saved in ' + get_directory() + '.', 'grey')
    elif chance == 2:
        return colored('Loading from ' + get_directory() + '...', 'blue')
    else:
        return colored('Scanning ' + get_directory() + '.', 'grey')

def get_babble(lines=None):
    # this returns a line of technobabble. 
    # if lines = an integer, generate a list of strings containing technobabble.

    if lines == None:
        if random.randint(1,3) == 1:
            return get_flavorful_text()
        else:
            return get_simple_text()
    else:
        result = []
        while len(result) < lines:
            chance = random.randint(0,100)
            if chance < 4 and len(result) < lines - 1:
                a,b = get_error_text()
                result.append(a)
                result.append(b)
            elif chance < 10 and len(result) < lines - 1:
                a,b = get_speed_text()
                result.append(a)
                result.append(b)

            elif chance < 20 and len(result) < lines - 1:
                a,b,t = get_timed_text()
                result.append(a)
                result.append(b)
            elif chance < 50:
                result.append(get_flavorful_text())
            elif chance < 55:
                result.append(get_directory_text())
            else:
                result.append(get_simple_text())
        return result
            
def babble(lines=1):
    #print technobabble, and do it lines number of times
    for i in range(0,lines):

        chance = random.randint(0,100)
        if chance < 4:
            a,b = get_error_text()
            print(a)
            time.sleep(random.random() * 4)
            print(b)

        elif chance < 10:
            a,b = get_speed_text()
            print(a)
            time.sleep(random.random() * 0.5)
            print(b)

        elif chance < 20:
            a,b,t = get_timed_text()
            print(a)
            time.sleep(t / 1000)
            print(b)

        elif chance < 50:
            print(get_flavorful_text())
        
        elif chance < 55:
            print(get_directory_text())

        else:
            print(get_simple_text())

        time.sleep(random.random())



if __name__ == '__main__':
    
    babble(100)
