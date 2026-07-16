# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage11
from . import Max140Text
from . import Max35Text
from . import TrueFalseIndicator

class AbortData6(base_types._BaseFieldType):

	__slots__ = ["_AbrtRsn", "_DispOutpt", "_TxSucss", "_XchgId"]
	@property
	def AbrtRsn(self):
		return self._AbrtRsn

	@AbrtRsn.setter
	def AbrtRsn(self, value):
		self._AbrtRsn = value if value is not None else base_types.UninitialisedField(self, 'AbrtRsn', Max140Text, False)

	@AbrtRsn.deleter
	def AbrtRsn(self):
		del self._AbrtRsn
		self._AbrtRsn = base_types.UninitialisedField(self, 'AbrtRsn', Max140Text, False)

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage11, False)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage11, False)

	@property
	def TxSucss(self):
		return self._TxSucss

	@TxSucss.setter
	def TxSucss(self, value):
		self._TxSucss = value if value is not None else base_types.UninitialisedField(self, 'TxSucss', TrueFalseIndicator, False)

	@TxSucss.deleter
	def TxSucss(self):
		del self._TxSucss
		self._TxSucss = base_types.UninitialisedField(self, 'TxSucss', TrueFalseIndicator, False)

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if value is not None else base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = base_types.UninitialisedField(self, 'XchgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AbrtRsn', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSucss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))