# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import ContactPersonal2
from . import Credentials3
from . import ISODate
from . import LocalData24
from . import Max105Text
from . import Max2NumericText
from . import Max35Text
from . import Max70Text
from . import TrueFalseIndicator

class Cardholder23(base_types._BaseFieldType):

	__slots__ = ["_AliasNm", "_BllgAdr", "_CmprssdAdr", "_CtctInf", "_Dsgnt", "_DtOfBirth", "_GvnNm", "_HghVal", "_Id", "_LastNm", "_LclData", "_MddlNm", "_Nm", "_NtlData", "_Ocptn", "_PrvtData", "_ShppgAdr"]
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
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if value is not None else base_types.UninitialisedField(self, 'BllgAdr', Address4, False)

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = base_types.UninitialisedField(self, 'BllgAdr', Address4, False)

	@property
	def CmprssdAdr(self):
		return self._CmprssdAdr

	@CmprssdAdr.setter
	def CmprssdAdr(self, value):
		self._CmprssdAdr = value if value is not None else base_types.UninitialisedField(self, 'CmprssdAdr', Max35Text, False)

	@CmprssdAdr.deleter
	def CmprssdAdr(self):
		del self._CmprssdAdr
		self._CmprssdAdr = base_types.UninitialisedField(self, 'CmprssdAdr', Max35Text, False)

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if value is not None else base_types.UninitialisedField(self, 'CtctInf', ContactPersonal2, False)

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = base_types.UninitialisedField(self, 'CtctInf', ContactPersonal2, False)

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
	def HghVal(self):
		return self._HghVal

	@HghVal.setter
	def HghVal(self, value):
		self._HghVal = value if value is not None else base_types.UninitialisedField(self, 'HghVal', TrueFalseIndicator, False)

	@HghVal.deleter
	def HghVal(self):
		del self._HghVal
		self._HghVal = base_types.UninitialisedField(self, 'HghVal', TrueFalseIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Credentials3, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Credentials3, True)

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
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData24, False)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData24, False)

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

	@property
	def ShppgAdr(self):
		return self._ShppgAdr

	@ShppgAdr.setter
	def ShppgAdr(self, value):
		self._ShppgAdr = value if value is not None else base_types.UninitialisedField(self, 'ShppgAdr', Address4, True)

	@ShppgAdr.deleter
	def ShppgAdr(self):
		del self._ShppgAdr
		self._ShppgAdr = base_types.UninitialisedField(self, 'ShppgAdr', Address4, True)

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