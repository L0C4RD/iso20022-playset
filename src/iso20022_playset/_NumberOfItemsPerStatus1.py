# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText
from . import ReportItemStatus1Code

class NumberOfItemsPerStatus1(base_types._BaseFieldType):

	__slots__ = ["_NbOfItms", "_Sts"]
	@property
	def NbOfItms(self):
		return self._NbOfItms

	@NbOfItms.setter
	def NbOfItms(self, value):
		self._NbOfItms = value if value is not None else base_types.UninitialisedField(self, 'NbOfItms', Max15NumericText, False)

	@NbOfItms.deleter
	def NbOfItms(self):
		del self._NbOfItms
		self._NbOfItms = base_types.UninitialisedField(self, 'NbOfItms', Max15NumericText, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ReportItemStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ReportItemStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfItms', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ReportItemStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))