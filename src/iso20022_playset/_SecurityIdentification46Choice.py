# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternateSecurityIdentification7
from . import BelgianIdentifier
from . import Bloomberg2Identifier
from . import CUSIPIdentifier
from . import ConsolidatedTapeAssociationIdentifier
from . import DTI2024Identifier
from . import DutchIdentifier
from . import EuroclearClearstreamIdentifier
from . import ISINOct2015Identifier
from . import QUICKIdentifier
from . import RICIdentifier
from . import SEDOLIdentifier
from . import SicovamIdentifier
from . import TickerIdentifier
from . import ValorenIdentifier
from . import WertpapierIdentifier

class SecurityIdentification46Choice(base_types._BaseFieldType):

	__slots__ = ["_Belgn", "_Blmbrg", "_CTA", "_CUSIP", "_Cmon", "_DTI", "_Dtch", "_ISIN", "_OthrPrtryId", "_QUICK", "_RIC", "_SCVM", "_SEDOL", "_TckrSymb", "_Vlrn", "_Wrtppr"]
	@property
	def Belgn(self):
		return self._Belgn

	@Belgn.setter
	def Belgn(self, value):
		self._Belgn = value if value is not None else base_types.UninitialisedField(self, 'Belgn', BelgianIdentifier, False)

	@Belgn.deleter
	def Belgn(self):
		del self._Belgn
		self._Belgn = base_types.UninitialisedField(self, 'Belgn', BelgianIdentifier, False)

	@property
	def Blmbrg(self):
		return self._Blmbrg

	@Blmbrg.setter
	def Blmbrg(self, value):
		self._Blmbrg = value if value is not None else base_types.UninitialisedField(self, 'Blmbrg', Bloomberg2Identifier, False)

	@Blmbrg.deleter
	def Blmbrg(self):
		del self._Blmbrg
		self._Blmbrg = base_types.UninitialisedField(self, 'Blmbrg', Bloomberg2Identifier, False)

	@property
	def CTA(self):
		return self._CTA

	@CTA.setter
	def CTA(self, value):
		self._CTA = value if value is not None else base_types.UninitialisedField(self, 'CTA', ConsolidatedTapeAssociationIdentifier, False)

	@CTA.deleter
	def CTA(self):
		del self._CTA
		self._CTA = base_types.UninitialisedField(self, 'CTA', ConsolidatedTapeAssociationIdentifier, False)

	@property
	def CUSIP(self):
		return self._CUSIP

	@CUSIP.setter
	def CUSIP(self, value):
		self._CUSIP = value if value is not None else base_types.UninitialisedField(self, 'CUSIP', CUSIPIdentifier, False)

	@CUSIP.deleter
	def CUSIP(self):
		del self._CUSIP
		self._CUSIP = base_types.UninitialisedField(self, 'CUSIP', CUSIPIdentifier, False)

	@property
	def Cmon(self):
		return self._Cmon

	@Cmon.setter
	def Cmon(self, value):
		self._Cmon = value if value is not None else base_types.UninitialisedField(self, 'Cmon', EuroclearClearstreamIdentifier, False)

	@Cmon.deleter
	def Cmon(self):
		del self._Cmon
		self._Cmon = base_types.UninitialisedField(self, 'Cmon', EuroclearClearstreamIdentifier, False)

	@property
	def DTI(self):
		return self._DTI

	@DTI.setter
	def DTI(self, value):
		self._DTI = value if value is not None else base_types.UninitialisedField(self, 'DTI', DTI2024Identifier, False)

	@DTI.deleter
	def DTI(self):
		del self._DTI
		self._DTI = base_types.UninitialisedField(self, 'DTI', DTI2024Identifier, False)

	@property
	def Dtch(self):
		return self._Dtch

	@Dtch.setter
	def Dtch(self, value):
		self._Dtch = value if value is not None else base_types.UninitialisedField(self, 'Dtch', DutchIdentifier, False)

	@Dtch.deleter
	def Dtch(self):
		del self._Dtch
		self._Dtch = base_types.UninitialisedField(self, 'Dtch', DutchIdentifier, False)

	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if value is not None else base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = base_types.UninitialisedField(self, 'ISIN', ISINOct2015Identifier, False)

	@property
	def OthrPrtryId(self):
		return self._OthrPrtryId

	@OthrPrtryId.setter
	def OthrPrtryId(self, value):
		self._OthrPrtryId = value if value is not None else base_types.UninitialisedField(self, 'OthrPrtryId', AlternateSecurityIdentification7, False)

	@OthrPrtryId.deleter
	def OthrPrtryId(self):
		del self._OthrPrtryId
		self._OthrPrtryId = base_types.UninitialisedField(self, 'OthrPrtryId', AlternateSecurityIdentification7, False)

	@property
	def QUICK(self):
		return self._QUICK

	@QUICK.setter
	def QUICK(self, value):
		self._QUICK = value if value is not None else base_types.UninitialisedField(self, 'QUICK', QUICKIdentifier, False)

	@QUICK.deleter
	def QUICK(self):
		del self._QUICK
		self._QUICK = base_types.UninitialisedField(self, 'QUICK', QUICKIdentifier, False)

	@property
	def RIC(self):
		return self._RIC

	@RIC.setter
	def RIC(self, value):
		self._RIC = value if value is not None else base_types.UninitialisedField(self, 'RIC', RICIdentifier, False)

	@RIC.deleter
	def RIC(self):
		del self._RIC
		self._RIC = base_types.UninitialisedField(self, 'RIC', RICIdentifier, False)

	@property
	def SCVM(self):
		return self._SCVM

	@SCVM.setter
	def SCVM(self, value):
		self._SCVM = value if value is not None else base_types.UninitialisedField(self, 'SCVM', SicovamIdentifier, False)

	@SCVM.deleter
	def SCVM(self):
		del self._SCVM
		self._SCVM = base_types.UninitialisedField(self, 'SCVM', SicovamIdentifier, False)

	@property
	def SEDOL(self):
		return self._SEDOL

	@SEDOL.setter
	def SEDOL(self, value):
		self._SEDOL = value if value is not None else base_types.UninitialisedField(self, 'SEDOL', SEDOLIdentifier, False)

	@SEDOL.deleter
	def SEDOL(self):
		del self._SEDOL
		self._SEDOL = base_types.UninitialisedField(self, 'SEDOL', SEDOLIdentifier, False)

	@property
	def TckrSymb(self):
		return self._TckrSymb

	@TckrSymb.setter
	def TckrSymb(self, value):
		self._TckrSymb = value if value is not None else base_types.UninitialisedField(self, 'TckrSymb', TickerIdentifier, False)

	@TckrSymb.deleter
	def TckrSymb(self):
		del self._TckrSymb
		self._TckrSymb = base_types.UninitialisedField(self, 'TckrSymb', TickerIdentifier, False)

	@property
	def Vlrn(self):
		return self._Vlrn

	@Vlrn.setter
	def Vlrn(self, value):
		self._Vlrn = value if value is not None else base_types.UninitialisedField(self, 'Vlrn', ValorenIdentifier, False)

	@Vlrn.deleter
	def Vlrn(self):
		del self._Vlrn
		self._Vlrn = base_types.UninitialisedField(self, 'Vlrn', ValorenIdentifier, False)

	@property
	def Wrtppr(self):
		return self._Wrtppr

	@Wrtppr.setter
	def Wrtppr(self, value):
		self._Wrtppr = value if value is not None else base_types.UninitialisedField(self, 'Wrtppr', WertpapierIdentifier, False)

	@Wrtppr.deleter
	def Wrtppr(self):
		del self._Wrtppr
		self._Wrtppr = base_types.UninitialisedField(self, 'Wrtppr', WertpapierIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Belgn', type=BelgianIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Blmbrg', type=Bloomberg2Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CTA', type=ConsolidatedTapeAssociationIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CUSIP', type=CUSIPIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmon', type=EuroclearClearstreamIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DTI', type=DTI2024Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dtch', type=DutchIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrPrtryId', type=AlternateSecurityIdentification7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QUICK', type=QUICKIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RIC', type=RICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SCVM', type=SicovamIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SEDOL', type=SEDOLIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TckrSymb', type=TickerIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Vlrn', type=ValorenIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wrtppr', type=WertpapierIdentifier, min=0, max=1, mutex_group=1, array=False),
	))