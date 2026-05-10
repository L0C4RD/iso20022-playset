from . import base_types
from .Max5000Binary import Max5000Binary
from .ContentInformationType10 import ContentInformationType10
from .AuthenticationMethod7Code import AuthenticationMethod7Code
from .OnLinePIN5 import OnLinePIN5
from .TrueFalseIndicator import TrueFalseIndicator

class CardholderAuthentication8(base_types._BaseFieldType):

	__slots__ = ["_CrdhldrOnLinePIN", "_AuthntcnVal", "_AuthntcnMtd", "_TknReqd", "_PrtctdAuthntcnVal"]
	@property
	def CrdhldrOnLinePIN(self):
		return self._CrdhldrOnLinePIN

	@CrdhldrOnLinePIN.setter
	def CrdhldrOnLinePIN(self, value):
		self._CrdhldrOnLinePIN = value if type(value) != auto else self.make_default("CrdhldrOnLinePIN")

	@CrdhldrOnLinePIN.deleter
	def CrdhldrOnLinePIN(self):
		del self._CrdhldrOnLinePIN
		self._CrdhldrOnLinePIN = None

	@property
	def AuthntcnVal(self):
		return self._AuthntcnVal

	@AuthntcnVal.setter
	def AuthntcnVal(self, value):
		self._AuthntcnVal = value if type(value) != auto else self.make_default("AuthntcnVal")

	@AuthntcnVal.deleter
	def AuthntcnVal(self):
		del self._AuthntcnVal
		self._AuthntcnVal = None

	@property
	def AuthntcnMtd(self):
		return self._AuthntcnMtd

	@AuthntcnMtd.setter
	def AuthntcnMtd(self, value):
		self._AuthntcnMtd = value if type(value) != auto else self.make_default("AuthntcnMtd")

	@AuthntcnMtd.deleter
	def AuthntcnMtd(self):
		del self._AuthntcnMtd
		self._AuthntcnMtd = None

	@property
	def TknReqd(self):
		return self._TknReqd

	@TknReqd.setter
	def TknReqd(self, value):
		self._TknReqd = value if type(value) != auto else self.make_default("TknReqd")

	@TknReqd.deleter
	def TknReqd(self):
		del self._TknReqd
		self._TknReqd = None

	@property
	def PrtctdAuthntcnVal(self):
		return self._PrtctdAuthntcnVal

	@PrtctdAuthntcnVal.setter
	def PrtctdAuthntcnVal(self, value):
		self._PrtctdAuthntcnVal = value if type(value) != auto else self.make_default("PrtctdAuthntcnVal")

	@PrtctdAuthntcnVal.deleter
	def PrtctdAuthntcnVal(self):
		del self._PrtctdAuthntcnVal
		self._PrtctdAuthntcnVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrdhldrOnLinePIN', type=OnLinePIN5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnVal', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnMtd', type=AuthenticationMethod7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TknReqd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdAuthntcnVal', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))

