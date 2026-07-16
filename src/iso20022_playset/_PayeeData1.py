# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import ContactPersonal2
from . import Credentials3
from . import FinancialInstitution10
from . import ISO8583AccountIdentifierTypeCode
from . import ISODate
from . import ISOMax3ACountryCode
from . import LocalData21
from . import Max105Text
from . import Max2NumericText
from . import Max35Text
from . import Max3Text
from . import Max70Text

class PayeeData1(base_types._BaseFieldType):

	__slots__ = ["_AcctIdr", "_AcctIdrTp", "_Adr", "_AliasNm", "_Crdntls", "_Ctct", "_CtryOfBirth", "_Dsgnt", "_DtOfBirth", "_FI", "_GvnNm", "_Id", "_LastNm", "_LclData", "_MddlNm", "_Nm", "_NtlData", "_Ntlty", "_NttyTp", "_Ocptn", "_PrvtData"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if value is not None else base_types.UninitialisedField(self, 'AcctIdr', Max70Text, False)

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = base_types.UninitialisedField(self, 'AcctIdr', Max70Text, False)

	@property
	def AcctIdrTp(self):
		return self._AcctIdrTp

	@AcctIdrTp.setter
	def AcctIdrTp(self, value):
		self._AcctIdrTp = value if value is not None else base_types.UninitialisedField(self, 'AcctIdrTp', ISO8583AccountIdentifierTypeCode, False)

	@AcctIdrTp.deleter
	def AcctIdrTp(self):
		del self._AcctIdrTp
		self._AcctIdrTp = base_types.UninitialisedField(self, 'AcctIdrTp', ISO8583AccountIdentifierTypeCode, False)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address4, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address4, False)

	@property
	def AliasNm(self):
		return self._AliasNm

	@AliasNm.setter
	def AliasNm(self, value):
		self._AliasNm = value if value is not None else base_types.UninitialisedField(self, 'AliasNm', Max70Text, False)

	@AliasNm.deleter
	def AliasNm(self):
		del self._AliasNm
		self._AliasNm = base_types.UninitialisedField(self, 'AliasNm', Max70Text, False)

	@property
	def Crdntls(self):
		return self._Crdntls

	@Crdntls.setter
	def Crdntls(self, value):
		self._Crdntls = value if value is not None else base_types.UninitialisedField(self, 'Crdntls', Credentials3, True)

	@Crdntls.deleter
	def Crdntls(self):
		del self._Crdntls
		self._Crdntls = base_types.UninitialisedField(self, 'Crdntls', Credentials3, True)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactPersonal2, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactPersonal2, False)

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if value is not None else base_types.UninitialisedField(self, 'CtryOfBirth', ISOMax3ACountryCode, False)

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = base_types.UninitialisedField(self, 'CtryOfBirth', ISOMax3ACountryCode, False)

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if value is not None else base_types.UninitialisedField(self, 'Dsgnt', Max2NumericText, False)

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = base_types.UninitialisedField(self, 'Dsgnt', Max2NumericText, False)

	@property
	def DtOfBirth(self):
		return self._DtOfBirth

	@DtOfBirth.setter
	def DtOfBirth(self, value):
		self._DtOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtOfBirth', ISODate, False)

	@DtOfBirth.deleter
	def DtOfBirth(self):
		del self._DtOfBirth
		self._DtOfBirth = base_types.UninitialisedField(self, 'DtOfBirth', ISODate, False)

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if value is not None else base_types.UninitialisedField(self, 'FI', FinancialInstitution10, False)

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = base_types.UninitialisedField(self, 'FI', FinancialInstitution10, False)

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if value is not None else base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

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
	def LastNm(self):
		return self._LastNm

	@LastNm.setter
	def LastNm(self, value):
		self._LastNm = value if value is not None else base_types.UninitialisedField(self, 'LastNm', Max35Text, False)

	@LastNm.deleter
	def LastNm(self):
		del self._LastNm
		self._LastNm = base_types.UninitialisedField(self, 'LastNm', Max35Text, False)

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData21, False)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData21, False)

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if value is not None else base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max105Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max105Text, False)

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
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if value is not None else base_types.UninitialisedField(self, 'Ntlty', ISOMax3ACountryCode, False)

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = base_types.UninitialisedField(self, 'Ntlty', ISOMax3ACountryCode, False)

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if value is not None else base_types.UninitialisedField(self, 'NttyTp', Max3Text, False)

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = base_types.UninitialisedField(self, 'NttyTp', Max3Text, False)

	@property
	def Ocptn(self):
		return self._Ocptn

	@Ocptn.setter
	def Ocptn(self, value):
		self._Ocptn = value if value is not None else base_types.UninitialisedField(self, 'Ocptn', Max35Text, False)

	@Ocptn.deleter
	def Ocptn(self):
		del self._Ocptn
		self._Ocptn = base_types.UninitialisedField(self, 'Ocptn', Max35Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctIdrTp', type=ISO8583AccountIdentifierTypeCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AliasNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Crdntls', type=Credentials3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfBirth', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FI', type=FinancialInstitution10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ntlty', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=Max3Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ocptn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
	))