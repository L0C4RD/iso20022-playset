# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max10MbText import Max10MbText
from ._Max20MbBinary import Max20MbBinary
from ._ProtectedData2 import ProtectedData2

class ReportContent2Choice(base_types._BaseFieldType):

	__slots__ = ["_Binry", "_PrtctdData", "_Txt"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if type(value) != base_types.auto else self.make_default("Binry")

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = None

	@property
	def PrtctdData(self):
		return self._PrtctdData

	@PrtctdData.setter
	def PrtctdData(self, value):
		self._PrtctdData = value if type(value) != base_types.auto else self.make_default("PrtctdData")

	@PrtctdData.deleter
	def PrtctdData(self):
		del self._PrtctdData
		self._PrtctdData = None

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != base_types.auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max20MbBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtctdData', type=ProtectedData2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Txt', type=Max10MbText, min=0, max=1, mutex_group=1, array=False),
	))