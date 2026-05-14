from . import base_types
from ._ATICAPartyType1Code import ATICAPartyType1Code
from ._ISODateTime import ISODateTime
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max140Text import Max140Text
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator

class PromotionData1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cd", "_Chanl", "_Ctgy", "_Desc", "_End", "_Prvdr", "_RedMtd", "_Start", "_Stckbl", "_TermsURL", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def Chanl(self):
		return self._Chanl

	@Chanl.setter
	def Chanl(self, value):
		self._Chanl = value if type(value) != base_types.auto else self.make_default("Chanl")

	@Chanl.deleter
	def Chanl(self):
		del self._Chanl
		self._Chanl = None

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != base_types.auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def End(self):
		return self._End

	@End.setter
	def End(self, value):
		self._End = value if type(value) != base_types.auto else self.make_default("End")

	@End.deleter
	def End(self):
		del self._End
		self._End = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != base_types.auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

	@property
	def RedMtd(self):
		return self._RedMtd

	@RedMtd.setter
	def RedMtd(self, value):
		self._RedMtd = value if type(value) != base_types.auto else self.make_default("RedMtd")

	@RedMtd.deleter
	def RedMtd(self):
		del self._RedMtd
		self._RedMtd = None

	@property
	def Start(self):
		return self._Start

	@Start.setter
	def Start(self, value):
		self._Start = value if type(value) != base_types.auto else self.make_default("Start")

	@Start.deleter
	def Start(self):
		del self._Start
		self._Start = None

	@property
	def Stckbl(self):
		return self._Stckbl

	@Stckbl.setter
	def Stckbl(self, value):
		self._Stckbl = value if type(value) != base_types.auto else self.make_default("Stckbl")

	@Stckbl.deleter
	def Stckbl(self):
		del self._Stckbl
		self._Stckbl = None

	@property
	def TermsURL(self):
		return self._TermsURL

	@TermsURL.setter
	def TermsURL(self, value):
		self._TermsURL = value if type(value) != base_types.auto else self.make_default("TermsURL")

	@TermsURL.deleter
	def TermsURL(self):
		del self._TermsURL
		self._TermsURL = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chanl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='End', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=ATICAPartyType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Start', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stckbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermsURL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

