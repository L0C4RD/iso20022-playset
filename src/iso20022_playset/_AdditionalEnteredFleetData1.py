# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Max350Text import Max350Text
from ._Max35NumericText import Max35NumericText

class AdditionalEnteredFleetData1(base_types._BaseFieldType):

	__slots__ = ["_AlphaNmrc", "_Nmrc", "_NtlData", "_PrvtData"]
	@property
	def AlphaNmrc(self):
		return self._AlphaNmrc

	@AlphaNmrc.setter
	def AlphaNmrc(self, value):
		self._AlphaNmrc = value if type(value) != base_types.auto else self.make_default("AlphaNmrc")

	@AlphaNmrc.deleter
	def AlphaNmrc(self):
		del self._AlphaNmrc
		self._AlphaNmrc = None

	@property
	def Nmrc(self):
		return self._Nmrc

	@Nmrc.setter
	def Nmrc(self, value):
		self._Nmrc = value if type(value) != base_types.auto else self.make_default("Nmrc")

	@Nmrc.deleter
	def Nmrc(self):
		del self._Nmrc
		self._Nmrc = None

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
		base_types.FieldEntry(name='AlphaNmrc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nmrc', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
	))