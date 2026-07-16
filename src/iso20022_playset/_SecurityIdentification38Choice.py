# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlternateIdentification1
from . import Bloomberg2Identifier
from . import ConsolidatedTapeAssociationIdentifier
from . import EuroclearClearstreamIdentifier
from . import ISINOct2015Identifier
from . import RICIdentifier
from . import TickerIdentifier

class SecurityIdentification38Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_Blmbrg", "_CTA", "_Cmon", "_ISIN", "_RIC", "_TckrSymb"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', AlternateIdentification1, False)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', AlternateIdentification1, False)

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
	def TckrSymb(self):
		return self._TckrSymb

	@TckrSymb.setter
	def TckrSymb(self, value):
		self._TckrSymb = value if value is not None else base_types.UninitialisedField(self, 'TckrSymb', TickerIdentifier, False)

	@TckrSymb.deleter
	def TckrSymb(self):
		del self._TckrSymb
		self._TckrSymb = base_types.UninitialisedField(self, 'TckrSymb', TickerIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=AlternateIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Blmbrg', type=Bloomberg2Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CTA', type=ConsolidatedTapeAssociationIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmon', type=EuroclearClearstreamIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RIC', type=RICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TckrSymb', type=TickerIdentifier, min=0, max=1, mutex_group=1, array=False),
	))