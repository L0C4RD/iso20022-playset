# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max15NumericText import Max15NumericText
from ._NumberOfTransactionsPerValidationRule5 import NumberOfTransactionsPerValidationRule5

class DetailedReportStatistics5(base_types._BaseFieldType):

	__slots__ = ["_NbOfRptsRjctdPerErr", "_TtlNbOfRpts", "_TtlNbOfRptsAccptd", "_TtlNbOfRptsRjctd"]
	@property
	def NbOfRptsRjctdPerErr(self):
		return self._NbOfRptsRjctdPerErr

	@NbOfRptsRjctdPerErr.setter
	def NbOfRptsRjctdPerErr(self, value):
		self._NbOfRptsRjctdPerErr = value if type(value) != base_types.auto else self.make_default("NbOfRptsRjctdPerErr")

	@NbOfRptsRjctdPerErr.deleter
	def NbOfRptsRjctdPerErr(self):
		del self._NbOfRptsRjctdPerErr
		self._NbOfRptsRjctdPerErr = None

	@property
	def TtlNbOfRpts(self):
		return self._TtlNbOfRpts

	@TtlNbOfRpts.setter
	def TtlNbOfRpts(self, value):
		self._TtlNbOfRpts = value if type(value) != base_types.auto else self.make_default("TtlNbOfRpts")

	@TtlNbOfRpts.deleter
	def TtlNbOfRpts(self):
		del self._TtlNbOfRpts
		self._TtlNbOfRpts = None

	@property
	def TtlNbOfRptsAccptd(self):
		return self._TtlNbOfRptsAccptd

	@TtlNbOfRptsAccptd.setter
	def TtlNbOfRptsAccptd(self, value):
		self._TtlNbOfRptsAccptd = value if type(value) != base_types.auto else self.make_default("TtlNbOfRptsAccptd")

	@TtlNbOfRptsAccptd.deleter
	def TtlNbOfRptsAccptd(self):
		del self._TtlNbOfRptsAccptd
		self._TtlNbOfRptsAccptd = None

	@property
	def TtlNbOfRptsRjctd(self):
		return self._TtlNbOfRptsRjctd

	@TtlNbOfRptsRjctd.setter
	def TtlNbOfRptsRjctd(self, value):
		self._TtlNbOfRptsRjctd = value if type(value) != base_types.auto else self.make_default("TtlNbOfRptsRjctd")

	@TtlNbOfRptsRjctd.deleter
	def TtlNbOfRptsRjctd(self):
		del self._TtlNbOfRptsRjctd
		self._TtlNbOfRptsRjctd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfRptsRjctdPerErr', type=NumberOfTransactionsPerValidationRule5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNbOfRpts', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRptsAccptd', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfRptsRjctd', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))