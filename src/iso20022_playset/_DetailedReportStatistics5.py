# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max15NumericText
from . import NumberOfTransactionsPerValidationRule5

class DetailedReportStatistics5(base_types._BaseFieldType):

	__slots__ = ["_NbOfRptsRjctdPerErr", "_TtlNbOfRpts", "_TtlNbOfRptsAccptd", "_TtlNbOfRptsRjctd"]
	@property
	def NbOfRptsRjctdPerErr(self):
		return self._NbOfRptsRjctdPerErr

	@NbOfRptsRjctdPerErr.setter
	def NbOfRptsRjctdPerErr(self, value):
		self._NbOfRptsRjctdPerErr = value if value is not None else base_types.UninitialisedField(self, 'NbOfRptsRjctdPerErr', NumberOfTransactionsPerValidationRule5, True)

	@NbOfRptsRjctdPerErr.deleter
	def NbOfRptsRjctdPerErr(self):
		del self._NbOfRptsRjctdPerErr
		self._NbOfRptsRjctdPerErr = base_types.UninitialisedField(self, 'NbOfRptsRjctdPerErr', NumberOfTransactionsPerValidationRule5, True)

	@property
	def TtlNbOfRpts(self):
		return self._TtlNbOfRpts

	@TtlNbOfRpts.setter
	def TtlNbOfRpts(self, value):
		self._TtlNbOfRpts = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRpts', Max15NumericText, False)

	@TtlNbOfRpts.deleter
	def TtlNbOfRpts(self):
		del self._TtlNbOfRpts
		self._TtlNbOfRpts = base_types.UninitialisedField(self, 'TtlNbOfRpts', Max15NumericText, False)

	@property
	def TtlNbOfRptsAccptd(self):
		return self._TtlNbOfRptsAccptd

	@TtlNbOfRptsAccptd.setter
	def TtlNbOfRptsAccptd(self, value):
		self._TtlNbOfRptsAccptd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRptsAccptd', Max15NumericText, False)

	@TtlNbOfRptsAccptd.deleter
	def TtlNbOfRptsAccptd(self):
		del self._TtlNbOfRptsAccptd
		self._TtlNbOfRptsAccptd = base_types.UninitialisedField(self, 'TtlNbOfRptsAccptd', Max15NumericText, False)

	@property
	def TtlNbOfRptsRjctd(self):
		return self._TtlNbOfRptsRjctd

	@TtlNbOfRptsRjctd.setter
	def TtlNbOfRptsRjctd(self, value):
		self._TtlNbOfRptsRjctd = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfRptsRjctd', Max15NumericText, False)

	@TtlNbOfRptsRjctd.deleter
	def TtlNbOfRptsRjctd(self):
		del self._TtlNbOfRptsRjctd
		self._TtlNbOfRptsRjctd = base_types.UninitialisedField(self, 'TtlNbOfRptsRjctd', Max15NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfRptsRjctdPerErr', type=NumberOfTransactionsPerValidationRule5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNbOfRpts', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRptsAccptd', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRptsRjctd', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))