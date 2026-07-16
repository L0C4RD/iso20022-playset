# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Number
from . import ReconciliationMessageType2Code

class MessageReconciliation3(base_types._BaseFieldType):

	__slots__ = ["_Cnt", "_OthrTp", "_Tp"]
	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if value is not None else base_types.UninitialisedField(self, 'Cnt', Number, False)

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = base_types.UninitialisedField(self, 'Cnt', Number, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ReconciliationMessageType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ReconciliationMessageType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnt', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReconciliationMessageType2Code, min=1, max=1, mutex_group=None, array=False),
	))