from . import base_types
from .CUSIPIdentifier import CUSIPIdentifier
from .ConsolidatedTapeAssociationIdentifier import ConsolidatedTapeAssociationIdentifier
from .EuroclearClearstreamIdentifier import EuroclearClearstreamIdentifier
from .DutchIdentifier import DutchIdentifier
from .AlternateSecurityIdentification7 import AlternateSecurityIdentification7
from .ISINOct2015Identifier import ISINOct2015Identifier
from .SEDOLIdentifier import SEDOLIdentifier
from .BelgianIdentifier import BelgianIdentifier
from .WertpapierIdentifier import WertpapierIdentifier
from .ValorenIdentifier import ValorenIdentifier
from .RICIdentifier import RICIdentifier
from .QUICKIdentifier import QUICKIdentifier
from .Bloomberg2Identifier import Bloomberg2Identifier
from .SicovamIdentifier import SicovamIdentifier
from .TickerIdentifier import TickerIdentifier

class SecurityIdentification25Choice(base_types._BaseFieldType):

	__slots__ = ["_CTA", "_Vlrn", "_QUICK", "_SCVM", "_TckrSymb", "_Belgn", "_Blmbrg", "_Cmon", "_ISIN", "_Wrtppr", "_OthrPrtryId", "_SEDOL", "_Dtch", "_CUSIP", "_RIC"]
	@property
	def CTA(self):
		return self._CTA

	@CTA.setter
	def CTA(self, value):
		self._CTA = value if type(value) != base_types.auto else self.make_default("CTA")

	@CTA.deleter
	def CTA(self):
		del self._CTA
		self._CTA = None

	@property
	def Vlrn(self):
		return self._Vlrn

	@Vlrn.setter
	def Vlrn(self, value):
		self._Vlrn = value if type(value) != base_types.auto else self.make_default("Vlrn")

	@Vlrn.deleter
	def Vlrn(self):
		del self._Vlrn
		self._Vlrn = None

	@property
	def QUICK(self):
		return self._QUICK

	@QUICK.setter
	def QUICK(self, value):
		self._QUICK = value if type(value) != base_types.auto else self.make_default("QUICK")

	@QUICK.deleter
	def QUICK(self):
		del self._QUICK
		self._QUICK = None

	@property
	def SCVM(self):
		return self._SCVM

	@SCVM.setter
	def SCVM(self, value):
		self._SCVM = value if type(value) != base_types.auto else self.make_default("SCVM")

	@SCVM.deleter
	def SCVM(self):
		del self._SCVM
		self._SCVM = None

	@property
	def TckrSymb(self):
		return self._TckrSymb

	@TckrSymb.setter
	def TckrSymb(self, value):
		self._TckrSymb = value if type(value) != base_types.auto else self.make_default("TckrSymb")

	@TckrSymb.deleter
	def TckrSymb(self):
		del self._TckrSymb
		self._TckrSymb = None

	@property
	def Belgn(self):
		return self._Belgn

	@Belgn.setter
	def Belgn(self, value):
		self._Belgn = value if type(value) != base_types.auto else self.make_default("Belgn")

	@Belgn.deleter
	def Belgn(self):
		del self._Belgn
		self._Belgn = None

	@property
	def Blmbrg(self):
		return self._Blmbrg

	@Blmbrg.setter
	def Blmbrg(self, value):
		self._Blmbrg = value if type(value) != base_types.auto else self.make_default("Blmbrg")

	@Blmbrg.deleter
	def Blmbrg(self):
		del self._Blmbrg
		self._Blmbrg = None

	@property
	def Cmon(self):
		return self._Cmon

	@Cmon.setter
	def Cmon(self, value):
		self._Cmon = value if type(value) != base_types.auto else self.make_default("Cmon")

	@Cmon.deleter
	def Cmon(self):
		del self._Cmon
		self._Cmon = None

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Wrtppr(self):
		return self._Wrtppr

	@Wrtppr.setter
	def Wrtppr(self, value):
		self._Wrtppr = value if type(value) != base_types.auto else self.make_default("Wrtppr")

	@Wrtppr.deleter
	def Wrtppr(self):
		del self._Wrtppr
		self._Wrtppr = None

	@property
	def OthrPrtryId(self):
		return self._OthrPrtryId

	@OthrPrtryId.setter
	def OthrPrtryId(self, value):
		self._OthrPrtryId = value if type(value) != base_types.auto else self.make_default("OthrPrtryId")

	@OthrPrtryId.deleter
	def OthrPrtryId(self):
		del self._OthrPrtryId
		self._OthrPrtryId = None

	@property
	def SEDOL(self):
		return self._SEDOL

	@SEDOL.setter
	def SEDOL(self, value):
		self._SEDOL = value if type(value) != base_types.auto else self.make_default("SEDOL")

	@SEDOL.deleter
	def SEDOL(self):
		del self._SEDOL
		self._SEDOL = None

	@property
	def Dtch(self):
		return self._Dtch

	@Dtch.setter
	def Dtch(self, value):
		self._Dtch = value if type(value) != base_types.auto else self.make_default("Dtch")

	@Dtch.deleter
	def Dtch(self):
		del self._Dtch
		self._Dtch = None

	@property
	def CUSIP(self):
		return self._CUSIP

	@CUSIP.setter
	def CUSIP(self, value):
		self._CUSIP = value if type(value) != base_types.auto else self.make_default("CUSIP")

	@CUSIP.deleter
	def CUSIP(self):
		del self._CUSIP
		self._CUSIP = None

	@property
	def RIC(self):
		return self._RIC

	@RIC.setter
	def RIC(self, value):
		self._RIC = value if type(value) != base_types.auto else self.make_default("RIC")

	@RIC.deleter
	def RIC(self):
		del self._RIC
		self._RIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CTA', type=ConsolidatedTapeAssociationIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Vlrn', type=ValorenIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QUICK', type=QUICKIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SCVM', type=SicovamIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TckrSymb', type=TickerIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Belgn', type=BelgianIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Blmbrg', type=Bloomberg2Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmon', type=EuroclearClearstreamIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wrtppr', type=WertpapierIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrPrtryId', type=AlternateSecurityIdentification7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SEDOL', type=SEDOLIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dtch', type=DutchIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CUSIP', type=CUSIPIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RIC', type=RICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

