# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._ContactPersonal2 import ContactPersonal2
from ._Credentials3 import Credentials3
from ._ISODate import ISODate
from ._LocalData24 import LocalData24
from ._Max105Text import Max105Text
from ._Max2NumericText import Max2NumericText
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._TrueFalseIndicator import TrueFalseIndicator

class Cardholder23(base_types._BaseFieldType):

	__slots__ = ["_AliasNm", "_BllgAdr", "_CmprssdAdr", "_CtctInf", "_Dsgnt", "_DtOfBirth", "_GvnNm", "_HghVal", "_Id", "_LastNm", "_LclData", "_MddlNm", "_Nm", "_NtlData", "_Ocptn", "_PrvtData", "_ShppgAdr"]
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
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if type(value) != base_types.auto else self.make_default("BllgAdr")

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = None

	@property
	def CmprssdAdr(self):
		return self._CmprssdAdr

	@CmprssdAdr.setter
	def CmprssdAdr(self, value):
		self._CmprssdAdr = value if type(value) != base_types.auto else self.make_default("CmprssdAdr")

	@CmprssdAdr.deleter
	def CmprssdAdr(self):
		del self._CmprssdAdr
		self._CmprssdAdr = None

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if type(value) != base_types.auto else self.make_default("CtctInf")

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = None

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
	def HghVal(self):
		return self._HghVal

	@HghVal.setter
	def HghVal(self, value):
		self._HghVal = value if type(value) != base_types.auto else self.make_default("HghVal")

	@HghVal.deleter
	def HghVal(self):
		del self._HghVal
		self._HghVal = None

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

	@property
	def ShppgAdr(self):
		return self._ShppgAdr

	@ShppgAdr.setter
	def ShppgAdr(self, value):
		self._ShppgAdr = value if type(value) != base_types.auto else self.make_default("ShppgAdr")

	@ShppgAdr.deleter
	def ShppgAdr(self):
		del self._ShppgAdr
		self._ShppgAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AliasNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgAdr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmprssdAdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctInf', type=ContactPersonal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghVal', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Credentials3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ocptn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShppgAdr', type=Address4, min=0, max=None, mutex_group=None, array=True),
	))