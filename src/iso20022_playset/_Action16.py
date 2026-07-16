# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionDestination1Code
from . import ActionType14Code
from . import AdditionalData1
from . import ContactPersonal1
from . import ISOMax3ALanguageCode
from . import Max140Binary
from . import Max35Text
from . import Max70Text
from . import OutputFormat4Code
from . import PartyType34Code

class Action16(base_types._BaseFieldType):

	__slots__ = ["_CertId", "_Cntt", "_Ctct", "_Dstn", "_DstnAdr", "_DstnTp", "_Frmt", "_Lang", "_OthrDstn", "_OthrDstnTp", "_OthrFrmt", "_OthrTp", "_Sgntr", "_Tp"]
	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if value is not None else base_types.UninitialisedField(self, 'CertId', Max70Text, False)

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = base_types.UninitialisedField(self, 'CertId', Max70Text, False)

	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if value is not None else base_types.UninitialisedField(self, 'Cntt', AdditionalData1, True)

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = base_types.UninitialisedField(self, 'Cntt', AdditionalData1, True)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactPersonal1, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactPersonal1, False)

	@property
	def Dstn(self):
		return self._Dstn

	@Dstn.setter
	def Dstn(self, value):
		self._Dstn = value if value is not None else base_types.UninitialisedField(self, 'Dstn', PartyType34Code, False)

	@Dstn.deleter
	def Dstn(self):
		del self._Dstn
		self._Dstn = base_types.UninitialisedField(self, 'Dstn', PartyType34Code, False)

	@property
	def DstnAdr(self):
		return self._DstnAdr

	@DstnAdr.setter
	def DstnAdr(self, value):
		self._DstnAdr = value if value is not None else base_types.UninitialisedField(self, 'DstnAdr', Max70Text, False)

	@DstnAdr.deleter
	def DstnAdr(self):
		del self._DstnAdr
		self._DstnAdr = base_types.UninitialisedField(self, 'DstnAdr', Max70Text, False)

	@property
	def DstnTp(self):
		return self._DstnTp

	@DstnTp.setter
	def DstnTp(self, value):
		self._DstnTp = value if value is not None else base_types.UninitialisedField(self, 'DstnTp', ActionDestination1Code, False)

	@DstnTp.deleter
	def DstnTp(self):
		del self._DstnTp
		self._DstnTp = base_types.UninitialisedField(self, 'DstnTp', ActionDestination1Code, False)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

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
	def OthrDstn(self):
		return self._OthrDstn

	@OthrDstn.setter
	def OthrDstn(self, value):
		self._OthrDstn = value if value is not None else base_types.UninitialisedField(self, 'OthrDstn', Max35Text, False)

	@OthrDstn.deleter
	def OthrDstn(self):
		del self._OthrDstn
		self._OthrDstn = base_types.UninitialisedField(self, 'OthrDstn', Max35Text, False)

	@property
	def OthrDstnTp(self):
		return self._OthrDstnTp

	@OthrDstnTp.setter
	def OthrDstnTp(self, value):
		self._OthrDstnTp = value if value is not None else base_types.UninitialisedField(self, 'OthrDstnTp', Max35Text, False)

	@OthrDstnTp.deleter
	def OthrDstnTp(self):
		del self._OthrDstnTp
		self._OthrDstnTp = base_types.UninitialisedField(self, 'OthrDstnTp', Max35Text, False)

	@property
	def OthrFrmt(self):
		return self._OthrFrmt

	@OthrFrmt.setter
	def OthrFrmt(self, value):
		self._OthrFrmt = value if value is not None else base_types.UninitialisedField(self, 'OthrFrmt', Max35Text, False)

	@OthrFrmt.deleter
	def OthrFrmt(self):
		del self._OthrFrmt
		self._OthrFrmt = base_types.UninitialisedField(self, 'OthrFrmt', Max35Text, False)

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
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if value is not None else base_types.UninitialisedField(self, 'Sgntr', Max140Binary, False)

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = base_types.UninitialisedField(self, 'Sgntr', Max140Binary, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ActionType14Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ActionType14Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CertId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntt', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dstn', type=PartyType34Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnTp', type=ActionDestination1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDstn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDstnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ActionType14Code, min=0, max=1, mutex_group=None, array=False),
	))