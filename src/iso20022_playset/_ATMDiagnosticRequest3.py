# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMEnvironment9
from . import ATMStatus2

class ATMDiagnosticRequest3(base_types._BaseFieldType):

	__slots__ = ["_ATMGblSts", "_Envt"]
	@property
	def ATMGblSts(self):
		return self._ATMGblSts

	@ATMGblSts.setter
	def ATMGblSts(self, value):
		self._ATMGblSts = value if value is not None else base_types.UninitialisedField(self, 'ATMGblSts', ATMStatus2, False)

	@ATMGblSts.deleter
	def ATMGblSts(self):
		del self._ATMGblSts
		self._ATMGblSts = base_types.UninitialisedField(self, 'ATMGblSts', ATMStatus2, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', ATMEnvironment9, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', ATMEnvironment9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMGblSts', type=ATMStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment9, min=1, max=1, mutex_group=None, array=False),
	))