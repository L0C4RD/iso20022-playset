# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._SecuritiesAccount19 import SecuritiesAccount19

class SecuritiesAccountReferenceDataChange2(base_types._BaseFieldType):

	__slots__ = ["_FldNm", "_NewFldVal", "_OdFldVal", "_OprTmStmp", "_SctiesAcctId"]
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

	@property
	def OprTmStmp(self):
		return self._OprTmStmp

	@OprTmStmp.setter
	def OprTmStmp(self, value):
		self._OprTmStmp = value if type(value) != base_types.auto else self.make_default("OprTmStmp")

	@OprTmStmp.deleter
	def OprTmStmp(self):
		del self._OprTmStmp
		self._OprTmStmp = None

	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if type(value) != base_types.auto else self.make_default("SctiesAcctId")

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FldNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctId', type=SecuritiesAccount19, min=1, max=1, mutex_group=None, array=False),
	))