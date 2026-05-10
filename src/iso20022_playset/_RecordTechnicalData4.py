from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._CountryCode import CountryCode
from ._Period4Choice import Period4Choice
from ._ISODateTime import ISODateTime
from ._MICIdentifier import MICIdentifier

class RecordTechnicalData4(base_types._BaseFieldType):

	__slots__ = ["_RlvntCmptntAuthrty", "_IncnsstncyInd", "_PblctnPrd", "_SubmissnDtTm", "_LastUpd", "_RlvntTradgVn", "_NvrPblshd"]
	@property
	def IncnsstncyInd(self):
		return self._IncnsstncyInd

	@IncnsstncyInd.setter
	def IncnsstncyInd(self, value):
		self._IncnsstncyInd = value if type(value) != base_types.auto else self.make_default("IncnsstncyInd")

	@IncnsstncyInd.deleter
	def IncnsstncyInd(self):
		del self._IncnsstncyInd
		self._IncnsstncyInd = None

	@property
	def LastUpd(self):
		return self._LastUpd

	@LastUpd.setter
	def LastUpd(self, value):
		self._LastUpd = value if type(value) != base_types.auto else self.make_default("LastUpd")

	@LastUpd.deleter
	def LastUpd(self):
		del self._LastUpd
		self._LastUpd = None

	@property
	def NvrPblshd(self):
		return self._NvrPblshd

	@NvrPblshd.setter
	def NvrPblshd(self, value):
		self._NvrPblshd = value if type(value) != base_types.auto else self.make_default("NvrPblshd")

	@NvrPblshd.deleter
	def NvrPblshd(self):
		del self._NvrPblshd
		self._NvrPblshd = None

	@property
	def PblctnPrd(self):
		return self._PblctnPrd

	@PblctnPrd.setter
	def PblctnPrd(self, value):
		self._PblctnPrd = value if type(value) != base_types.auto else self.make_default("PblctnPrd")

	@PblctnPrd.deleter
	def PblctnPrd(self):
		del self._PblctnPrd
		self._PblctnPrd = None

	@property
	def RlvntCmptntAuthrty(self):
		return self._RlvntCmptntAuthrty

	@RlvntCmptntAuthrty.setter
	def RlvntCmptntAuthrty(self, value):
		self._RlvntCmptntAuthrty = value if type(value) != base_types.auto else self.make_default("RlvntCmptntAuthrty")

	@RlvntCmptntAuthrty.deleter
	def RlvntCmptntAuthrty(self):
		del self._RlvntCmptntAuthrty
		self._RlvntCmptntAuthrty = None

	@property
	def RlvntTradgVn(self):
		return self._RlvntTradgVn

	@RlvntTradgVn.setter
	def RlvntTradgVn(self, value):
		self._RlvntTradgVn = value if type(value) != base_types.auto else self.make_default("RlvntTradgVn")

	@RlvntTradgVn.deleter
	def RlvntTradgVn(self):
		del self._RlvntTradgVn
		self._RlvntTradgVn = None

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if type(value) != base_types.auto else self.make_default("SubmissnDtTm")

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncnsstncyInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpd', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NvrPblshd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblctnPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlvntCmptntAuthrty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlvntTradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

