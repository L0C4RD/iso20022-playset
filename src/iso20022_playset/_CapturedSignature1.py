# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max2MBBinary
from . import Max35Text
from . import Max500Text

class CapturedSignature1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ImgData", "_ImgFrmt", "_ImgRef"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@property
	def ImgData(self):
		return self._ImgData

	@ImgData.setter
	def ImgData(self, value):
		self._ImgData = value if value is not None else base_types.UninitialisedField(self, 'ImgData', Max2MBBinary, False)

	@ImgData.deleter
	def ImgData(self):
		del self._ImgData
		self._ImgData = base_types.UninitialisedField(self, 'ImgData', Max2MBBinary, False)

	@property
	def ImgFrmt(self):
		return self._ImgFrmt

	@ImgFrmt.setter
	def ImgFrmt(self, value):
		self._ImgFrmt = value if value is not None else base_types.UninitialisedField(self, 'ImgFrmt', Max35Text, False)

	@ImgFrmt.deleter
	def ImgFrmt(self):
		del self._ImgFrmt
		self._ImgFrmt = base_types.UninitialisedField(self, 'ImgFrmt', Max35Text, False)

	@property
	def ImgRef(self):
		return self._ImgRef

	@ImgRef.setter
	def ImgRef(self, value):
		self._ImgRef = value if value is not None else base_types.UninitialisedField(self, 'ImgRef', Max500Text, False)

	@ImgRef.deleter
	def ImgRef(self):
		del self._ImgRef
		self._ImgRef = base_types.UninitialisedField(self, 'ImgRef', Max500Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgData', type=Max2MBBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgFrmt', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ImgRef', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
	))