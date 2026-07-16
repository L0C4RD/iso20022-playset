# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import AdditionalServiceType3Code
from . import ISO8583AdditionalServiceResultCode
from . import Max10Text

class AdditionalService3(base_types._BaseFieldType):

	__slots__ = ["_Dtl", "_Rslt", "_SubTp", "_Tp"]
	@property
	def Dtl(self):
		return self._Dtl

	@Dtl.setter
	def Dtl(self, value):
		self._Dtl = value if value is not None else base_types.UninitialisedField(self, 'Dtl', ATICALaxProcessing, False)

	@Dtl.deleter
	def Dtl(self):
		del self._Dtl
		self._Dtl = base_types.UninitialisedField(self, 'Dtl', ATICALaxProcessing, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', ISO8583AdditionalServiceResultCode, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', ISO8583AdditionalServiceResultCode, False)

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if value is not None else base_types.UninitialisedField(self, 'SubTp', Max10Text, False)

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = base_types.UninitialisedField(self, 'SubTp', Max10Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AdditionalServiceType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AdditionalServiceType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dtl', type=ATICALaxProcessing, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=ISO8583AdditionalServiceResultCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AdditionalServiceType3Code, min=1, max=1, mutex_group=None, array=False),
	))