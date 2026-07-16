# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import ISOMax3ACountryCode
from . import Max35Text
from . import PartyType17Code
from . import PartyType18Code

class Traceability10(base_types._BaseFieldType):

	__slots__ = ["_Assgnr", "_Ctry", "_DtTmIn", "_DtTmOut", "_Id", "_OthrTp", "_ShrtNm", "_Tp"]
	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', PartyType18Code, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', PartyType18Code, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', ISOMax3ACountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', ISOMax3ACountryCode, False)

	@property
	def DtTmIn(self):
		return self._DtTmIn

	@DtTmIn.setter
	def DtTmIn(self, value):
		self._DtTmIn = value if value is not None else base_types.UninitialisedField(self, 'DtTmIn', ISODateTime, False)

	@DtTmIn.deleter
	def DtTmIn(self):
		del self._DtTmIn
		self._DtTmIn = base_types.UninitialisedField(self, 'DtTmIn', ISODateTime, False)

	@property
	def DtTmOut(self):
		return self._DtTmOut

	@DtTmOut.setter
	def DtTmOut(self, value):
		self._DtTmOut = value if value is not None else base_types.UninitialisedField(self, 'DtTmOut', ISODateTime, False)

	@DtTmOut.deleter
	def DtTmOut(self):
		del self._DtTmOut
		self._DtTmOut = base_types.UninitialisedField(self, 'DtTmOut', ISODateTime, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PartyType17Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PartyType17Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnr', type=PartyType18Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTmIn', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTmOut', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PartyType17Code, min=0, max=1, mutex_group=None, array=False),
	))