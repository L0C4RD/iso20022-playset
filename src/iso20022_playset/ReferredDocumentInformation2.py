import base_types
import ActiveCurrencyAndAmount
import Max35Text
import ISODate
import ReferredDocumentType1

class ReferredDocumentInformation2(base_types._BaseFieldType):

	__slots__ = ["_RltdDt", "_DocAmt", "_Tp", "_DocNb"]
	@property
	def RltdDt(self):
		return self._RltdDt

	@RltdDt.setter
	def RltdDt(self, value):
		self._RltdDt = value if type(value) != auto else self.make_default("RltdDt")

	@RltdDt.deleter
	def RltdDt(self):
		del self._RltdDt
		self._RltdDt = None

	@property
	def DocAmt(self):
		return self._DocAmt

	@DocAmt.setter
	def DocAmt(self, value):
		self._DocAmt = value if type(value) != auto else self.make_default("DocAmt")

	@DocAmt.deleter
	def DocAmt(self):
		del self._DocAmt
		self._DocAmt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DocNb(self):
		return self._DocNb

	@DocNb.setter
	def DocNb(self, value):
		self._DocNb = value if type(value) != auto else self.make_default("DocNb")

	@DocNb.deleter
	def DocNb(self):
		del self._DocNb
		self._DocNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RltdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReferredDocumentType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

