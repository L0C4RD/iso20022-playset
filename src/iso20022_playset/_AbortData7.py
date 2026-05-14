# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActionMessage12 import ActionMessage12
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator

class AbortData7(base_types._BaseFieldType):

	__slots__ = ["_AbrtRsn", "_DispOutpt", "_TxSucss", "_XchgId"]
	@property
	def AbrtRsn(self):
		return self._AbrtRsn

	@AbrtRsn.setter
	def AbrtRsn(self, value):
		self._AbrtRsn = value if type(value) != base_types.auto else self.make_default("AbrtRsn")

	@AbrtRsn.deleter
	def AbrtRsn(self):
		del self._AbrtRsn
		self._AbrtRsn = None

	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if type(value) != base_types.auto else self.make_default("DispOutpt")

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = None

	@property
	def TxSucss(self):
		return self._TxSucss

	@TxSucss.setter
	def TxSucss(self, value):
		self._TxSucss = value if type(value) != base_types.auto else self.make_default("TxSucss")

	@TxSucss.deleter
	def TxSucss(self):
		del self._TxSucss
		self._TxSucss = None

	@property
	def XchgId(self):
		return self._XchgId

	@XchgId.setter
	def XchgId(self, value):
		self._XchgId = value if type(value) != base_types.auto else self.make_default("XchgId")

	@XchgId.deleter
	def XchgId(self):
		del self._XchgId
		self._XchgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AbrtRsn', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSucss', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))