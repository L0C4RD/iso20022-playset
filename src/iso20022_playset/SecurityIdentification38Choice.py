from . import base_types
from .TickerIdentifier import TickerIdentifier
from .AlternateIdentification1 import AlternateIdentification1
from .ISINOct2015Identifier import ISINOct2015Identifier
from .EuroclearClearstreamIdentifier import EuroclearClearstreamIdentifier
from .RICIdentifier import RICIdentifier
from .ConsolidatedTapeAssociationIdentifier import ConsolidatedTapeAssociationIdentifier
from .Bloomberg2Identifier import Bloomberg2Identifier

class SecurityIdentification38Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmon", "_Blmbrg", "_CTA", "_ISIN", "_TckrSymb", "_RIC", "_AltrnId"]
	@property
	def Cmon(self):
		return self._Cmon

	@Cmon.setter
	def Cmon(self, value):
		self._Cmon = value if type(value) != auto else self.make_default("Cmon")

	@Cmon.deleter
	def Cmon(self):
		del self._Cmon
		self._Cmon = None

	@property
	def Blmbrg(self):
		return self._Blmbrg

	@Blmbrg.setter
	def Blmbrg(self, value):
		self._Blmbrg = value if type(value) != auto else self.make_default("Blmbrg")

	@Blmbrg.deleter
	def Blmbrg(self):
		del self._Blmbrg
		self._Blmbrg = None

	@property
	def CTA(self):
		return self._CTA

	@CTA.setter
	def CTA(self, value):
		self._CTA = value if type(value) != auto else self.make_default("CTA")

	@CTA.deleter
	def CTA(self):
		del self._CTA
		self._CTA = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def TckrSymb(self):
		return self._TckrSymb

	@TckrSymb.setter
	def TckrSymb(self, value):
		self._TckrSymb = value if type(value) != auto else self.make_default("TckrSymb")

	@TckrSymb.deleter
	def TckrSymb(self):
		del self._TckrSymb
		self._TckrSymb = None

	@property
	def RIC(self):
		return self._RIC

	@RIC.setter
	def RIC(self, value):
		self._RIC = value if type(value) != auto else self.make_default("RIC")

	@RIC.deleter
	def RIC(self):
		del self._RIC
		self._RIC = None

	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmon', type=EuroclearClearstreamIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Blmbrg', type=Bloomberg2Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CTA', type=ConsolidatedTapeAssociationIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TckrSymb', type=TickerIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RIC', type=RICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AltrnId', type=AlternateIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

