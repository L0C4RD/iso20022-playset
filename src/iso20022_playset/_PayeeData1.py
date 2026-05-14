# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._ContactPersonal2 import ContactPersonal2
from ._Credentials3 import Credentials3
from ._FinancialInstitution10 import FinancialInstitution10
from ._ISO8583AccountIdentifierTypeCode import ISO8583AccountIdentifierTypeCode
from ._ISODate import ISODate
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._LocalData21 import LocalData21
from ._Max105Text import Max105Text
from ._Max2NumericText import Max2NumericText
from ._Max35Text import Max35Text
from ._Max3Text import Max3Text
from ._Max70Text import Max70Text

class PayeeData1(base_types._BaseFieldType):

	__slots__ = ["_AcctIdr", "_AcctIdrTp", "_Adr", "_AliasNm", "_Crdntls", "_Ctct", "_CtryOfBirth", "_Dsgnt", "_DtOfBirth", "_FI", "_GvnNm", "_Id", "_LastNm", "_LclData", "_MddlNm", "_Nm", "_NtlData", "_Ntlty", "_NttyTp", "_Ocptn", "_PrvtData"]
	@property
	def AcctIdr(self):
		return self._AcctIdr

	@AcctIdr.setter
	def AcctIdr(self, value):
		self._AcctIdr = value if type(value) != base_types.auto else self.make_default("AcctIdr")

	@AcctIdr.deleter
	def AcctIdr(self):
		del self._AcctIdr
		self._AcctIdr = None

	@property
	def AcctIdrTp(self):
		return self._AcctIdrTp

	@AcctIdrTp.setter
	def AcctIdrTp(self, value):
		self._AcctIdrTp = value if type(value) != base_types.auto else self.make_default("AcctIdrTp")

	@AcctIdrTp.deleter
	def AcctIdrTp(self):
		del self._AcctIdrTp
		self._AcctIdrTp = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def AliasNm(self):
		return self._AliasNm

	@AliasNm.setter
	def AliasNm(self, value):
		self._AliasNm = value if type(value) != base_types.auto else self.make_default("AliasNm")

	@AliasNm.deleter
	def AliasNm(self):
		del self._AliasNm
		self._AliasNm = None

	@property
	def Crdntls(self):
		return self._Crdntls

	@Crdntls.setter
	def Crdntls(self, value):
		self._Crdntls = value if type(value) != base_types.auto else self.make_default("Crdntls")

	@Crdntls.deleter
	def Crdntls(self):
		del self._Crdntls
		self._Crdntls = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != base_types.auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def CtryOfBirth(self):
		return self._CtryOfBirth

	@CtryOfBirth.setter
	def CtryOfBirth(self, value):
		self._CtryOfBirth = value if type(value) != base_types.auto else self.make_default("CtryOfBirth")

	@CtryOfBirth.deleter
	def CtryOfBirth(self):
		del self._CtryOfBirth
		self._CtryOfBirth = None

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != base_types.auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

	@property
	def DtOfBirth(self):
		return self._DtOfBirth

	@DtOfBirth.setter
	def DtOfBirth(self, value):
		self._DtOfBirth = value if type(value) != base_types.auto else self.make_default("DtOfBirth")

	@DtOfBirth.deleter
	def DtOfBirth(self):
		del self._DtOfBirth
		self._DtOfBirth = None

	@property
	def FI(self):
		return self._FI

	@FI.setter
	def FI(self, value):
		self._FI = value if type(value) != base_types.auto else self.make_default("FI")

	@FI.deleter
	def FI(self):
		del self._FI
		self._FI = None

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if type(value) != base_types.auto else self.make_default("GvnNm")

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LastNm(self):
		return self._LastNm

	@LastNm.setter
	def LastNm(self, value):
		self._LastNm = value if type(value) != base_types.auto else self.make_default("LastNm")

	@LastNm.deleter
	def LastNm(self):
		del self._LastNm
		self._LastNm = None

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != base_types.auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if type(value) != base_types.auto else self.make_default("MddlNm")

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if type(value) != base_types.auto else self.make_default("Ntlty")

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = None

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if type(value) != base_types.auto else self.make_default("NttyTp")

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = None

	@property
	def Ocptn(self):
		return self._Ocptn

	@Ocptn.setter
	def Ocptn(self, value):
		self._Ocptn = value if type(value) != base_types.auto else self.make_default("Ocptn")

	@Ocptn.deleter
	def Ocptn(self):
		del self._Ocptn
		self._Ocptn = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

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