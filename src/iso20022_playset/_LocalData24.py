# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import CardholderName2
from . import ISOMax3ALanguageCode
from . import LocalAddress1
from . import LocalAddress2
from . import Max140Text
from . import Max35Text
from . import Max70Text

class LocalData24(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_AliasNm", "_Lang", "_NcodgFrmt", "_Nm", "_NtlData", "_Ocptn", "_PrvtData", "_ShppgAdr"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', LocalAddress2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', LocalAddress2, False)

	@property
	def AliasNm(self):
		return self._AliasNm

	@AliasNm.setter
	def AliasNm(self, value):
		self._AliasNm = value if value is not None else base_types.UninitialisedField(self, 'AliasNm', Max140Text, False)

	@AliasNm.deleter
	def AliasNm(self):
		del self._AliasNm
		self._AliasNm = base_types.UninitialisedField(self, 'AliasNm', Max140Text, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@property
	def NcodgFrmt(self):
		return self._NcodgFrmt

	@NcodgFrmt.setter
	def NcodgFrmt(self, value):
		self._NcodgFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@NcodgFrmt.deleter
	def NcodgFrmt(self):
		del self._NcodgFrmt
		self._NcodgFrmt = base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', CardholderName2, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', CardholderName2, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def Ocptn(self):
		return self._Ocptn

	@Ocptn.setter
	def Ocptn(self, value):
		self._Ocptn = value if value is not None else base_types.UninitialisedField(self, 'Ocptn', Max70Text, False)

	@Ocptn.deleter
	def Ocptn(self):
		del self._Ocptn
		self._Ocptn = base_types.UninitialisedField(self, 'Ocptn', Max70Text, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def ShppgAdr(self):
		return self._ShppgAdr

	@ShppgAdr.setter
	def ShppgAdr(self, value):
		self._ShppgAdr = value if value is not None else base_types.UninitialisedField(self, 'ShppgAdr', LocalAddress1, True)

	@ShppgAdr.deleter
	def ShppgAdr(self):
		del self._ShppgAdr
		self._ShppgAdr = base_types.UninitialisedField(self, 'ShppgAdr', LocalAddress1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=LocalAddress2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AliasNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=CardholderName2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ocptn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShppgAdr', type=LocalAddress1, min=0, max=None, mutex_group=None, array=True),
	))