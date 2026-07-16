# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10MbText
from . import Max20MbBinary
from . import ProtectedData2

class ReportContent2Choice(base_types._BaseFieldType):

	__slots__ = ["_Binry", "_PrtctdData", "_Txt"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if value is not None else base_types.UninitialisedField(self, 'Binry', Max20MbBinary, False)

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = base_types.UninitialisedField(self, 'Binry', Max20MbBinary, False)

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdData', ProtectedData2, False)

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = base_types.UninitialisedField(self, 'PrtctdData', ProtectedData2, False)

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if value is not None else base_types.UninitialisedField(self, 'Txt', Max10MbText, False)

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = base_types.UninitialisedField(self, 'Txt', Max10MbText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max20MbBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Txt', type=Max10MbText, min=0, max=1, mutex_group=1, array=False),
	))