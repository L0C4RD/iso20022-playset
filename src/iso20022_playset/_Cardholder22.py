# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Address2
from . import CardholderName3
from . import ContactPersonal1
from . import Credentials3
from . import ISODate
from . import LocalData13
from . import TrueFalseIndicator

class Cardholder22(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Adr", "_CtctInf", "_DtOfBirth", "_HghVal", "_Id", "_LclData", "_Nm"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address2, False)

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if value is not None else base_types.UninitialisedField(self, 'CtctInf', ContactPersonal1, False)

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = base_types.UninitialisedField(self, 'CtctInf', ContactPersonal1, False)

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
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData13, False)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData13, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', CardholderName3, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', CardholderName3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctInf', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghVal', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Credentials3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LclData', type=LocalData13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=CardholderName3, min=0, max=1, mutex_group=None, array=False),
	))