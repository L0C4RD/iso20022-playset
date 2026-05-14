# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text

class UpdateLogProprietary1(base_types._BaseFieldType):

	__slots__ = ["_FldNm", "_NewFldVal", "_OdFldVal"]
	@property
	def FldNm(self):
		return self._FldNm

	@FldNm.setter
	def FldNm(self, value):
		self._FldNm = value if type(value) != base_types.auto else self.make_default("FldNm")

	@FldNm.deleter
	def FldNm(self):
		del self._FldNm
		self._FldNm = None

	@property
	def NewFldVal(self):
		return self._NewFldVal

	@NewFldVal.setter
	def NewFldVal(self, value):
		self._NewFldVal = value if type(value) != base_types.auto else self.make_default("NewFldVal")

	@NewFldVal.deleter
	def NewFldVal(self):
		del self._NewFldVal
		self._NewFldVal = None

	@property
	def OdFldVal(self):
		return self._OdFldVal

	@OdFldVal.setter
	def OdFldVal(self, value):
		self._OdFldVal = value if type(value) != base_types.auto else self.make_default("OdFldVal")

	@OdFldVal.deleter
	def OdFldVal(self):
		del self._OdFldVal
		self._OdFldVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FldNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))