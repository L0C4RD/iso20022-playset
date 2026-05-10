import base_types
import Max35Text
import ATMCustomerProfile1Code
import LanguageCode

class ATMCustomerProfile6(base_types._BaseFieldType):

	__slots__ = ["_CstmrId", "_PrflRef", "_PrefrdLang", "_RtrvlMd"]
	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if type(value) != auto else self.make_default("CstmrId")

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = None

	@property
	def PrflRef(self):
		return self._PrflRef

	@PrflRef.setter
	def PrflRef(self, value):
		self._PrflRef = value if type(value) != auto else self.make_default("PrflRef")

	@PrflRef.deleter
	def PrflRef(self):
		del self._PrflRef
		self._PrflRef = None

	@property
	def PrefrdLang(self):
		return self._PrefrdLang

	@PrefrdLang.setter
	def PrefrdLang(self, value):
		self._PrefrdLang = value if type(value) != auto else self.make_default("PrefrdLang")

	@PrefrdLang.deleter
	def PrefrdLang(self):
		del self._PrefrdLang
		self._PrefrdLang = None

	@property
	def RtrvlMd(self):
		return self._RtrvlMd

	@RtrvlMd.setter
	def RtrvlMd(self, value):
		self._RtrvlMd = value if type(value) != auto else self.make_default("RtrvlMd")

	@RtrvlMd.deleter
	def RtrvlMd(self):
		del self._RtrvlMd
		self._RtrvlMd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrefrdLang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrvlMd', type=ATMCustomerProfile1Code, min=1, max=1, mutex_group=None, array=False),
	))

