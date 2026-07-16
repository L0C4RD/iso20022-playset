# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount40
from . import ClearingSystemIdentification3Choice
from . import SettlementMethod2Code

class SettlementInstruction14(base_types._BaseFieldType):

	__slots__ = ["_ClrSys", "_SttlmAcct", "_SttlmMtd"]
	@property
	def ClrSys(self):
		return self._ClrSys

	@ClrSys.setter
	def ClrSys(self, value):
		self._ClrSys = value if value is not None else base_types.UninitialisedField(self, 'ClrSys', ClearingSystemIdentification3Choice, False)

	@ClrSys.deleter
	def ClrSys(self):
		del self._ClrSys
		self._ClrSys = base_types.UninitialisedField(self, 'ClrSys', ClearingSystemIdentification3Choice, False)

	@property
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if value is not None else base_types.UninitialisedField(self, 'SttlmAcct', CashAccount40, False)

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = base_types.UninitialisedField(self, 'SttlmAcct', CashAccount40, False)

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if value is not None else base_types.UninitialisedField(self, 'SttlmMtd', SettlementMethod2Code, False)

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = base_types.UninitialisedField(self, 'SttlmMtd', SettlementMethod2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSys', type=ClearingSystemIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=SettlementMethod2Code, min=1, max=1, mutex_group=None, array=False),
	))