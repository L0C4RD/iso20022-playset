# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2048Text

class SettlementFailureReason2(base_types._BaseFieldType):

	__slots__ = ["_EffcncyImprvmt", "_MainRsns"]
	@property
	def EffcncyImprvmt(self):
		return self._EffcncyImprvmt

	@EffcncyImprvmt.setter
	def EffcncyImprvmt(self, value):
		self._EffcncyImprvmt = value if value is not None else base_types.UninitialisedField(self, 'EffcncyImprvmt', Max2048Text, False)

	@EffcncyImprvmt.deleter
	def EffcncyImprvmt(self):
		del self._EffcncyImprvmt
		self._EffcncyImprvmt = base_types.UninitialisedField(self, 'EffcncyImprvmt', Max2048Text, False)

	@property
	def MainRsns(self):
		return self._MainRsns

	@MainRsns.setter
	def MainRsns(self, value):
		self._MainRsns = value if value is not None else base_types.UninitialisedField(self, 'MainRsns', Max2048Text, False)

	@MainRsns.deleter
	def MainRsns(self):
		del self._MainRsns
		self._MainRsns = base_types.UninitialisedField(self, 'MainRsns', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EffcncyImprvmt', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainRsns', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
	))