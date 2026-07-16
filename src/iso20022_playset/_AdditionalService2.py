# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import AdditionalServiceResult1Code
from . import AdditionalServiceType2Code
from . import Max35Text

class AdditionalService2(base_types._BaseFieldType):

	__slots__ = ["_OthrRslt", "_OthrTp", "_Rslt", "_SvcDtl", "_Tp"]
	@property
	def OthrRslt(self):
		return self._OthrRslt

	@OthrRslt.setter
	def OthrRslt(self, value):
		self._OthrRslt = value if value is not None else base_types.UninitialisedField(self, 'OthrRslt', Max35Text, False)

	@OthrRslt.deleter
	def OthrRslt(self):
		del self._OthrRslt
		self._OthrRslt = base_types.UninitialisedField(self, 'OthrRslt', Max35Text, False)

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
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', AdditionalServiceResult1Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', AdditionalServiceResult1Code, False)

	@property
	def SvcDtl(self):
		return self._SvcDtl

	@SvcDtl.setter
	def SvcDtl(self, value):
		self._SvcDtl = value if value is not None else base_types.UninitialisedField(self, 'SvcDtl', AdditionalData1, True)

	@SvcDtl.deleter
	def SvcDtl(self):
		del self._SvcDtl
		self._SvcDtl = base_types.UninitialisedField(self, 'SvcDtl', AdditionalData1, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AdditionalServiceType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AdditionalServiceType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrRslt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=AdditionalServiceResult1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDtl', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=AdditionalServiceType2Code, min=1, max=1, mutex_group=None, array=False),
	))