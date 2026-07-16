# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardholderAuthentication17
from . import LanguageCode
from . import Max35Text
from . import Max45Text
from . import Max70Text
from . import MobileData6
from . import PersonIdentification15
from . import PostalAddress22
from . import TransactionVerificationResult4
from . import Vehicle1

class Cardholder21(base_types._BaseFieldType):

	__slots__ = ["_Authntcn", "_BllgAdr", "_Id", "_Lang", "_MobData", "_Nm", "_PrsnlData", "_ShppgAdr", "_TripNb", "_TxVrfctnRslt", "_Vhcl"]
	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if value is not None else base_types.UninitialisedField(self, 'Authntcn', CardholderAuthentication17, True)

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = base_types.UninitialisedField(self, 'Authntcn', CardholderAuthentication17, True)

	@property
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if value is not None else base_types.UninitialisedField(self, 'BllgAdr', PostalAddress22, False)

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = base_types.UninitialisedField(self, 'BllgAdr', PostalAddress22, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PersonIdentification15, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PersonIdentification15, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', LanguageCode, False)

	@property
	def MobData(self):
		return self._MobData

	@MobData.setter
	def MobData(self, value):
		self._MobData = value if value is not None else base_types.UninitialisedField(self, 'MobData', MobileData6, True)

	@MobData.deleter
	def MobData(self):
		del self._MobData
		self._MobData = base_types.UninitialisedField(self, 'MobData', MobileData6, True)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max45Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max45Text, False)

	@property
	def PrsnlData(self):
		return self._PrsnlData

	@PrsnlData.setter
	def PrsnlData(self, value):
		self._PrsnlData = value if value is not None else base_types.UninitialisedField(self, 'PrsnlData', Max70Text, False)

	@PrsnlData.deleter
	def PrsnlData(self):
		del self._PrsnlData
		self._PrsnlData = base_types.UninitialisedField(self, 'PrsnlData', Max70Text, False)

	@property
	def ShppgAdr(self):
		return self._ShppgAdr

	@ShppgAdr.setter
	def ShppgAdr(self, value):
		self._ShppgAdr = value if value is not None else base_types.UninitialisedField(self, 'ShppgAdr', PostalAddress22, False)

	@ShppgAdr.deleter
	def ShppgAdr(self):
		del self._ShppgAdr
		self._ShppgAdr = base_types.UninitialisedField(self, 'ShppgAdr', PostalAddress22, False)

	@property
	def TripNb(self):
		return self._TripNb

	@TripNb.setter
	def TripNb(self, value):
		self._TripNb = value if value is not None else base_types.UninitialisedField(self, 'TripNb', Max35Text, False)

	@TripNb.deleter
	def TripNb(self):
		del self._TripNb
		self._TripNb = base_types.UninitialisedField(self, 'TripNb', Max35Text, False)

	@property
	def TxVrfctnRslt(self):
		return self._TxVrfctnRslt

	@TxVrfctnRslt.setter
	def TxVrfctnRslt(self, value):
		self._TxVrfctnRslt = value if value is not None else base_types.UninitialisedField(self, 'TxVrfctnRslt', TransactionVerificationResult4, True)

	@TxVrfctnRslt.deleter
	def TxVrfctnRslt(self):
		del self._TxVrfctnRslt
		self._TxVrfctnRslt = base_types.UninitialisedField(self, 'TxVrfctnRslt', TransactionVerificationResult4, True)

	@property
	def Vhcl(self):
		return self._Vhcl

	@Vhcl.setter
	def Vhcl(self, value):
		self._Vhcl = value if value is not None else base_types.UninitialisedField(self, 'Vhcl', Vehicle1, False)

	@Vhcl.deleter
	def Vhcl(self):
		del self._Vhcl
		self._Vhcl = base_types.UninitialisedField(self, 'Vhcl', Vehicle1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authntcn', type=CardholderAuthentication17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PersonIdentification15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=LanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobData', type=MobileData6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max45Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlData', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShppgAdr', type=PostalAddress22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TripNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxVrfctnRslt', type=TransactionVerificationResult4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vhcl', type=Vehicle1, min=0, max=1, mutex_group=None, array=False),
	))