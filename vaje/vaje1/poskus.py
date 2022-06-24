# =============================================================================
# 0/1 nahrbtnik
#
# Pri reševanju problema 0/1 nahrbtnika imamo opravka z množicami $S_i$ in
# $Z_i$. Predstavili jih bomo s seznami parov, ki so urejeni naraščajoče po
# prvih komponentah.
# =====================================================================@029306=
# 1. podnaloga
# Sestavi funkcijo `preveri(s)`, ki za parameter `s` dobi seznam parov.
# Funkcija naj ugotovi, ali ta seznam lahko (teoretično) predstavlja neko
# množico $S$ za nek problem 0/1 nahrbtnika.
# 
#     >>> preveri([(0,0),(3,7),(4,9),(8,12),(11,17),(20,33)])
#     True
# =============================================================================
def preveri(s):
    if len(s) == 0:
        return False
    if len(s) == 1 and s[0] != (0, 0):
        return False
    for i in range(1, len(s)):
        if s[i][0] <= s[i - 1][0]:
            return False
        if s[i][1] < s[i - 1][1]:
            return False
    return True
# =====================================================================@029307=
# 2. podnaloga
# Sestavi funkcijo `sestaviZ(s, predmet)`, ki za neko množico $S_i$ in predmet,
# podan s parom `(velikost, vrednost)`, sestavi in vrne množico $Z_{i+1}$.
# 
#     >>> sestaviZ([(0,0),(1,1),(2,2),(3,3)], (4,4))
#     [(4,4),(5,5),(6,6),(7,7)]
# =============================================================================
def sestaviZ(s, predmet):
    nov_s = s[:]
    for i in range(len(s)):
        nov_s[i] =(s[i][0] + predmet[0], s[i][1] + predmet[1])
    return nov_s
# =====================================================================@029308=
# 3. podnaloga
# Sestavi funkcijo `sestaviS(s, z)`, ki iz množic $S_i$ in $Z_{i+1}$ sestavi in
# vrne množico $S_{i+1}$.
# 
#     >>> sestaviS([(0,0),(11,6),(40,9),(51,15)], [(16,4),(27,10),(56,13),(67,19)])
#     [(0,0),(11,6),(27,10),(51,15),(67,19)]
# 
# Bi lahko kaj "poenostavil", če bi poznal velikost nahrbtnika?
# =============================================================================
def sestaviS(s, z):
    nov = s + z
    nov.sort()
    i = 1
    while i < len(nov):
        if nov[i][0] == nov[i - 1][0]:
            if nov[i][1] >= nov[i - 1][1]:
                nov = nov[:i - 1] + nov[i:]
                i -= 1
            else:
                nov = nov[:i] + nov[i + 1:]
        else:
            if nov[i][1] <= nov[i - 1][1]:
                nov = nov[:i] + nov[i + 1:]
            else:
                i += 1
    return nov
            
# =====================================================================@029309=
# 4. podnaloga
# Sestavi funkcijo `mnoziceS(predmeti)`, ki za dani seznam predmetov, pri čemer
# je vsak predmet predstavljen s parom `(velikost, vrednost)`, sestavi in vrne
# seznam vseh množic $S$.
# 
#     >>> mnoziceS([(2,3),(4,5),(4,7),(6,8)])
#     [[(0,0)],[(0,0),(2,3)],[(0,0),(2,3),(4,5),(6,8)],[(0,0),(2,3),(4,7),
#        (6,10),(8,12),(10,15)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15),
#        (12,18),(14,20),(16,23)]]
# =============================================================================
def mnoziceS(predmeti, vrniz = False):
    s = [[(0, 0)]]
    z = []
    for i in range(len(predmeti)):
        z.append(sestaviZ(s[i], predmeti[i]))
        s.append(sestaviS(s[i], z[i]))
    if vrniz:
        return s, z
    return s
# =====================================================================@029310=
# 5. podnaloga
# Sestavi funkcijo `nahrbtnik01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika, kjer je `predmeti` seznam predmetov, predstavljen kot prej,
# `velikost` pa velikost nahrtnika. Funkcija naj vrne skupno velikost in
# vrednost predmetov, ki jih damo v nahrbtnik.
# 
#     >>> nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 9)
#     (8,12)
# =============================================================================
def nahrbtnik01(predmeti, velikost):
    s = mnoziceS(predmeti)[-1]
    for i in range(len(s)):
        if s[i][0] > velikost:
            return s[i - 1]
    return s[-1]
# =====================================================================@029311=
# 6. podnaloga
# Sestavi funkcijo `resitev01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika kot pri prejšnji podnalogi, le da vrne seznam ničel in enic, ki
# določajo, katere predmete moramo izbrati. Če je rešitev več, naj vrne
# katerokoli izmed njih.
# 
#     >>> resitev01([(2,3),(4,5),(4,7),(6,8)], 9)
#     [0, 1, 1, 0]
# =============================================================================
def resitev01(predmeti, velikost):
    if len(predmeti) == 1:
        if velikost < predmeti[0][0]:
            return [0]
        else:
            return [1]
    vr = nahrbtnik01(predmeti, velikost)
    s, z = mnoziceS(predmeti, True)
    if vr in z[-1] and vr in s[-2]:
        return resitev01(predmeti[:-1], velikost) + [0]
    elif vr in s[-2] and vr not in z[-1]:
        return resitev01(predmeti[:-1], velikost) + [0]
    else:
        return resitev01(predmeti[:-1], velikost - predmeti[-1][0]) + [1]
# =====================================================================@029312=
# 7. podnaloga
# Sestavi funkcijo `resitve01(predmeti, velikost)`, ki reši problem 0/1
# nahrbtnika kot pri prejšnji podnalogi, le da vrne seznam vseh možnih rešitev.
# Vrstni red rešitev v seznamu ni pomemben.
# 
#     >>> resitve01([(2,4),(4,5),(4,7),(6,8)], 9)
#     [[0, 1, 1, 0], [1, 0, 0, 1]]
# =============================================================================
def resitve01(predmeti, velikost):
        if len(predmeti) == 1:
            if velikost < predmeti[0][0]:
                return [[0]]
            else:
                return [[1]]
        vr = nahrbtnik01(predmeti, velikost)
        s, z = mnoziceS(predmeti, True)
        if vr in z[-1] and vr in s[-2]:
            vrni1 = resitve01(predmeti[:-1], velikost)
            vrni2 = resitve01(predmeti[:-1], velikost - predmeti[-1][0])
            for i in range(len(vrni1)):
                vrni1[i].append(0)
            for i in range(len(vrni2)):
                vrni2[i].append(1)
            return vrni1 + vrni2
        elif vr in s[-2] and vr not in z[-1]:
            vrni = resitve01(predmeti[:-1], velikost)
            for i in range(len(vrni)):
                vrni[i].append(0)
            return vrni
        else:
            vrni = resitve01(predmeti[:-1], velikost - predmeti[-1][0])
            for i in range(len(vrni)):
                vrni[i].append(1)
            return vrni
# =====================================================================@029313=
# 8. podnaloga
# Sestavi funkcijo `resitev0n(predmeti, velikost)`, ki reši malo spremenjen
# problem nahrbtnika. Vzamemo lahko več enakih predmetov, koliko posameznih
# predmetov imamo na voljo pa je dodano pri opisu posameznega predmeta. Namesto
# para (velikost, cena) imamo torej trojko (velikost, cena, količina). Funkcija
# naj vrne seznam celih števil, ki določajo, koliko katerih predmetov moramo
# vzeti. Če je rešitev več, naj vrne katerokoli izmed njih. Namig: pretvori
# problem na običajen problem 0/1 nahrbtnika.
# 
#     >>> resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 15)
#     [2, 0, 1, 1]
# =============================================================================





































































































# ============================================================================@

'Če vam Python sporoča, da je v tej vrstici sintaktična napaka,'
'se napaka v resnici skriva v zadnjih vrsticah vaše kode.'

'Kode od tu naprej NE SPREMINJAJTE!'


















































import json, os, re, sys, shutil, traceback, urllib.error, urllib.request


import io, sys
from contextlib import contextmanager

class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end='')
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end='')
        return line


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part['solution'].strip() != ''

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part['valid'] = True
            part['feedback'] = []
            part['secret'] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part['feedback'].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part['valid'] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed))
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted([(Check.clean(k, digits, typed), Check.clean(v, digits, typed)) for (k, v) in x.items()])
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get('clean', clean)
        Check.current_part['secret'].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error('Izraz {0} vrne {1!r} namesto {2!r}.',
                        expression, actual_result, expected_result)
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error('Namestiti morate numpy.')
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error('Ta funkcija je namenjena testiranju za tip np.ndarray.')

        if env is None:
            env = dict()
        env.update({'np': np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error("Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                        type(expected_result).__name__, type(actual_result).__name__)
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error("Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.", exp_shape, act_shape)
            return False
        try:
            np.testing.assert_allclose(expected_result, actual_result, atol=tol, rtol=tol)
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        exec(code, global_env)
        errors = []
        for (x, v) in expected_state.items():
            if x not in global_env:
                errors.append('morajo nastaviti spremenljivko {0}, vendar je ne'.format(x))
            elif clean(global_env[x]) != clean(v):
                errors.append('nastavijo {0} na {1!r} namesto na {2!r}'.format(x, global_env[x], v))
        if errors:
            Check.error('Ukazi\n{0}\n{1}.', statements,  ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, 'w', encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part['feedback'][:]
        yield
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n    '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}', filename, '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part['feedback'][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get('stringio')('\n'.join(content) + '\n')
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part['feedback'][len(old_feedback):]
        Check.current_part['feedback'] = old_feedback
        if new_feedback:
            new_feedback = ['\n  '.join(error.split('\n')) for error in new_feedback]
            Check.error('Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}', '\n  '.join(content), '\n- '.join(new_feedback))

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get('encoding', encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error('Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}', filename, (line_width - 7) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(expression, global_env)
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal:
            return True
        else:
            Check.error('Program izpiše{0}  namesto:\n  {1}', (line_width - 13) * ' ', '\n  '.join(diff))
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ['\n']
        else:
            expected_lines += (actual_len - expected_len) * ['\n']
        equal = True
        line_width = max(len(actual_line.rstrip()) for actual_line in actual_lines + ['Program izpiše'])
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append('{0} {1} {2}'.format(out.ljust(line_width), '|' if out == given else '*', given))
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get('update_env', update_env):
            global_env = dict(global_env)
        global_env.update(Check.get('env', env))
        return global_env

    @staticmethod
    def generator(expression, expected_values, should_stop=None, further_iter=None, clean=None, env=None, update_env=None):
        from types import GeneratorType
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get('clean', clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error("Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                                iteration, expression, actual_value, expected_value)
                    return False
            for _ in range(Check.get('further_iter', further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get('should_stop', should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print('{0}. podnaloga je brez rešitve.'.format(i + 1))
            elif not part['valid']:
                print('{0}. podnaloga nima veljavne rešitve.'.format(i + 1))
            else:
                print('{0}. podnaloga ima veljavno rešitev.'.format(i + 1))
            for message in part['feedback']:
                print('  - {0}'.format('\n    '.join(message.splitlines())))

    settings_stack = [{
        'clean': clean.__func__,
        'encoding': None,
        'env': {},
        'further_iter': 0,
        'should_stop': False,
        'stringio': VisibleStringIO,
        'update_env': False,
    }]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs))
                             if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get('env'))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get('stringio'):
            yield
        else:
            with Check.set(stringio=stringio):
                yield


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding='utf-8') as f:
            source = f.read()
        part_regex = re.compile(
            r'# =+@(?P<part>\d+)=\s*\n' # beginning of header
            r'(\s*#( [^\n]*)?\n)+?'     # description
            r'\s*# =+\s*?\n'            # end of header
            r'(?P<solution>.*?)'        # solution
            r'(?=\n\s*# =+@)',          # beginning of next part
            flags=re.DOTALL | re.MULTILINE
        )
        parts = [{
            'part': int(match.group('part')),
            'solution': match.group('solution')
        } for match in part_regex.finditer(source)]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]['solution'] = parts[-1]['solution'].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = '{0}.{1}'.format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    'part': part['part'],
                    'solution': part['solution'],
                    'valid': part['valid'],
                    'secret': [x for (x, _) in part['secret']],
                    'feedback': json.dumps(part['feedback']),
                }
                if 'token' in part:
                    submitted_part['token'] = part['token']
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode('utf-8')
        headers = {
            'Authorization': token,
            'content-type': 'application/json'
        }
        import ssl
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request, context=ctx)
        return json.loads(response.read().decode('utf-8'))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response['attempts']:
            part['feedback'] = json.loads(part['feedback'])
            updates[part['part']] = part
        for part in old_parts:
            valid_before = part['valid']
            part.update(updates.get(part['part'], {}))
            valid_after = part['valid']
            if valid_before and not valid_after:
                wrong_index = response['wrong_indices'].get(str(part['part']))
                if wrong_index is not None:
                    hint = part['secret'][wrong_index][1]
                    if hint:
                        part['feedback'].append('Namig: {}'.format(hint))


    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMwNn0:1n7HcQ:BNhZYQYg8xNo0GhNq70Bs9Q3kXc'
        try:
            test_data = [
                ('preveri([(0,0),(3,7),(4,9),(8,12),(11,17),(20,33)])', True),
                ('preveri([])', False),
                ('preveri([(0,0)])', True),
                ('preveri([(1,2)])', False),
                ('preveri([(0,0),(5,9)])', True),
                ('preveri([(0,0),(-5,9)])', False),
                ('preveri([(0,0),(5,-9)])', False),
                ('preveri([(0,0),(0,9)])', False),
                ('preveri([(0,0),(45,6),(56,12),(72,20),(98,19),(96,21),(103,23),(102,25),(128,28),(144,32)])', False),
                ('preveri([(0,0),(45,6),(56,12),(72,16),(98,19),(96,21),(103,23),(102,25),(128,28),(144,32)])', False),
                ('preveri([(0,0),(45,6),(56,12),(72,16),(98,19),(99,21),(103,23),(106,25),(128,28),(144,32)])', True),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMwN30:1n7HcQ:oPDlxMRTrO483e5bwD7MuChGgQE'
        try:
            test_data = [
                ('sestaviZ([(0,0),(1,1),(2,2),(3,3)], (4,4))', [(4,4),(5,5),(6,6),(7,7)]),
                ('sestaviZ([(0,0),(11,6),(27,10),(51,15),(67,19)], (32,7))', [(32,7),(43,13),(59,17),(83,22),(99,26)]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMwOH0:1n7HcQ:igs-1a5Bl1ygrvEE5xKs71zP1tA'
        try:
            test_data = [
                ('sestaviS([(0,0)], [(11,6)])', [(0,0),(11,6)]),
                ('sestaviS([(0,0),(11,6)], [(40,9),(51,15)])', [(0,0),(11,6),(40,9),(51,15)]),
                ('sestaviS([(0,0),(11,6),(40,9),(51,15)], [(16,4),(27,10),(56,13),(67,19)])', [(0,0),(11,6),(27,10),(51,15),(67,19)]),
                ('sestaviS([(0,0),(11,6),(27,10),(51,15),(67,19)], [(32,7),(43,13),(59,17),(83,22),(99,26)])', [(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26)]),
                ('sestaviS([(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26)], [(45,6),(56,12),(72,16),(88,19),(96,21),(104,23),(112,25),(128,28),(144,32)])', [(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26),(128,28),(144,32)]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMwOX0:1n7HcQ:uigDMg-jWBhWb9KptKPhM4KIC0c'
        try:
            test_data = [
                ('mnoziceS([(2,3),(4,5),(4,7),(6,8)])', [[(0,0)],[(0,0),(2,3)],[(0,0),(2,3),(4,5),(6,8)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15)],[(0,0),(2,3),(4,7),(6,10),(8,12),(10,15),(12,18),(14,20),(16,23)]]),
                ('mnoziceS([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)])', [[(0,0)],[(0,0),(11,6)],[(0,0),(11,6),(40,9),(51,15)],[(0,0),(11,6),(27,10),(51,15),(67,19)],[(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26)],[(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26),(128,28),(144,32)],[(0,0),(11,6),(27,10),(43,13),(51,15),(59,17),(67,19),(83,22),(99,26),(128,28),(131,29),(144,32),(147,33),(176,35),(192,39)],[(0,0),(9,5),(11,6),(20,11),(36,15),(52,18),(60,20),(68,22),(76,24),(92,27),(108,31),(137,33),(140,34),(153,37),(156,38),(185,40),(201,44)],[(0,0),(9,5),(11,6),(20,11),(36,15),(52,18),(60,20),(68,22),(76,24),(92,27),(104,29),(108,31),(120,33),(136,36),(152,40),(181,42),(184,43),(197,46),(200,47),(229,49),(245,53)]]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMxMH0:1n7HcQ:yiwxWmVRTxaYDaVn9GWf7Nku75A'
        try:
            test_data = [
                ('nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 9)', (8,12)),
                ('nahrbtnik01([(2,3),(4,5),(4,7),(6,8)], 13)', (12,18)),
                ('nahrbtnik01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 160)', (152, 40)),
                ('nahrbtnik01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 300)', (245, 53)),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMxMX0:1n7HcQ:wmIruHugVapivl3lF1Hpjl8usAg'
        try:
            test_data = [
                ('resitev01([(2,3),(4,5),(4,7),(6,8)], 9)', [0, 1, 1, 0]),
                ('resitev01([(2,3),(4,5),(4,7),(6,8)], 13)', [1, 0, 1, 1]),
                ('resitev01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 160)', [1, 1, 1, 1, 0, 0, 1, 1]),
                ('resitev01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 300)', [1, 1, 1, 1, 1, 1, 1, 1]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMxMn0:1n7HcQ:-hXCbeLHA2M3Df9kZ0_o6j6DMTA'
        try:
            test_data = [
                ('resitve01([(2,3),(4,5),(4,7),(6,8)], 9)', [[0, 1, 1, 0]]),
                ('resitve01([(2,3),(4,5),(4,7),(6,8)], 13)', [[1, 0, 1, 1]]),
                ('sorted(resitve01([(2,4),(4,5),(4,7),(6,8)], 9))', [[0, 1, 1, 0], [1, 0, 0, 1]]),
                ('resitve01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 160)', [[1, 1, 1, 1, 0, 0, 1, 1]]),
                ('resitve01([(11,6),(40,9),(16,4),(32,7),(45,6),(48,7),(9,5),(44,9)], 300)', [[1, 1, 1, 1, 1, 1, 1, 1]]),
                ('sorted(resitve01([(10,8),(42,7),(16,9),(45,4),(45,3),(68,24),(9,5),(44,4)], 70))', [[0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0]]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    if Check.part():
        Check.current_part['token'] = 'eyJ1c2VyIjo0NzI2LCJwYXJ0IjoyOTMxM30:1n7HcQ:gXOLuagAwDVwCi5UXq216lQ_vRM'
        try:
            test_data = [
                ('resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 15)', [2, 0, 1, 1]),
                ('resitev0n([(2,3,2),(4,5,3),(4,7,1),(6,8,2)], 25)', [2, 1, 1, 2]),
                ('resitev0n([(11,3,2),(40,9,2),(16,4,1),(32,7,3),(45,6,2),(48,7,1),(9,5,5),(44,9,1)], 200)', [2, 2, 1, 1, 0, 0, 5, 0]),
            ]
            for data in test_data:
                if not Check.equal(*data):
                    break
        except:
            Check.error("Testi sprožijo izjemo\n  {0}",
                        "\n  ".join(traceback.format_exc().split("\n"))[:-2])

    print('Shranjujem rešitve na strežnik... ', end="")
    try:
        url = 'https://www.projekt-tomo.si/api/attempts/submit/'
        token = 'Token cf78acbaa0c32e40a183408733ada0357aec8483'
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = ('\n'
                   '-------------------------------------------------------------------\n'
                   'PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n'
                   'Preberite napako in poskusite znova ali se posvetujte z asistentom.\n'
                   '-------------------------------------------------------------------\n')
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print('Rešitve so shranjene.')
        update_attempts(Check.parts, response)
        if 'update' in response:
            print('Updating file... ', end="")
            backup_filename = backup(filename)
            with open(__file__, 'w', encoding='utf-8') as f:
                f.write(response['update'])
            print('Previous file has been renamed to {0}.'.format(backup_filename))
            print('If the file did not refresh in your editor, close and reopen it.')
    Check.summarize()

if __name__ == '__main__':
    _validate_current_file()
