# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICAPartyType1Code
from . import ISODateTime
from . import ImpliedCurrencyAndAmount
from . import Max140Text
from . import Max256Text
from . import Max35Text
from . import TrueFalseIndicator

class PromotionData1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cd", "_Chanl", "_Ctgy", "_Desc", "_End", "_Prvdr", "_RedMtd", "_Start", "_Stckbl", "_TermsURL", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max35Text, False)

	@property
	def Chanl(self):
		return self._Chanl

	@Chanl.setter
	def Chanl(self, value):
		self._Chanl = value if value is not None else base_types.UninitialisedField(self, 'Chanl', Max35Text, False)

	@Chanl.deleter
	def Chanl(self):
		del self._Chanl
		self._Chanl = base_types.UninitialisedField(self, 'Chanl', Max35Text, False)

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', Max35Text, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', Max35Text, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def End(self):
		return self._End

	@End.setter
	def End(self, value):
		self._End = value if value is not None else base_types.UninitialisedField(self, 'End', ISODateTime, False)

	@End.deleter
	def End(self):
		del self._End
		self._End = base_types.UninitialisedField(self, 'End', ISODateTime, False)

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if value is not None else base_types.UninitialisedField(self, 'Prvdr', ATICAPartyType1Code, False)

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = base_types.UninitialisedField(self, 'Prvdr', ATICAPartyType1Code, False)

	@property
	def RedMtd(self):
		return self._RedMtd

	@RedMtd.setter
	def RedMtd(self, value):
		self._RedMtd = value if value is not None else base_types.UninitialisedField(self, 'RedMtd', Max35Text, False)

	@RedMtd.deleter
	def RedMtd(self):
		del self._RedMtd
		self._RedMtd = base_types.UninitialisedField(self, 'RedMtd', Max35Text, False)

	@property
	def Start(self):
		return self._Start

	@Start.setter
	def Start(self, value):
		self._Start = value if value is not None else base_types.UninitialisedField(self, 'Start', ISODateTime, False)

	@Start.deleter
	def Start(self):
		del self._Start
		self._Start = base_types.UninitialisedField(self, 'Start', ISODateTime, False)

	@property
	def Stckbl(self):
		return self._Stckbl

	@Stckbl.setter
	def Stckbl(self, value):
		self._Stckbl = value if value is not None else base_types.UninitialisedField(self, 'Stckbl', TrueFalseIndicator, False)

	@Stckbl.deleter
	def Stckbl(self):
		del self._Stckbl
		self._Stckbl = base_types.UninitialisedField(self, 'Stckbl', TrueFalseIndicator, False)

	@property
	def TermsURL(self):
		return self._TermsURL

	@TermsURL.setter
	def TermsURL(self, value):
		self._TermsURL = value if value is not None else base_types.UninitialisedField(self, 'TermsURL', Max256Text, False)

	@TermsURL.deleter
	def TermsURL(self):
		del self._TermsURL
		self._TermsURL = base_types.UninitialisedField(self, 'TermsURL', Max256Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

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