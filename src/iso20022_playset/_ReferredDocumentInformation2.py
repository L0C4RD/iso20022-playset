# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ISODate
from . import Max35Text
from . import ReferredDocumentType1

class ReferredDocumentInformation2(base_types._BaseFieldType):

	__slots__ = ["_DocAmt", "_DocNb", "_RltdDt", "_Tp"]
	@property
	def DocAmt(self):
		return self._DocAmt

	@DocAmt.setter
	def DocAmt(self, value):
		self._DocAmt = value if value is not None else base_types.UninitialisedField(self, 'DocAmt', ActiveCurrencyAndAmount, False)

	@DocAmt.deleter
	def DocAmt(self):
		del self._DocAmt
		self._DocAmt = base_types.UninitialisedField(self, 'DocAmt', ActiveCurrencyAndAmount, False)

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if value is not None else base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = base_types.UninitialisedField(self, 'DocNb', Max35Text, False)

	@property
	def RltdDt(self):
		return self._RltdDt

	@RltdDt.setter
	def RltdDt(self, value):
		self._RltdDt = value if value is not None else base_types.UninitialisedField(self, 'RltdDt', ISODate, False)

	@RltdDt.deleter
	def RltdDt(self):
		del self._RltdDt
		self._RltdDt = base_types.UninitialisedField(self, 'RltdDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ReferredDocumentType1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ReferredDocumentType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DocAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReferredDocumentType1, min=0, max=1, mutex_group=None, array=False),
	))