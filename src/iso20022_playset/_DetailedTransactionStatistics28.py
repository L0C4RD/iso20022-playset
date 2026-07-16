# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AbnormalValuesData4
from . import Number

class DetailedTransactionStatistics28(base_types._BaseFieldType):

	__slots__ = ["_NbOfDerivsRptd", "_NbOfDerivsRptdWthOtlrs", "_Wrnngs"]
	@property
	def NbOfDerivsRptd(self):
		return self._NbOfDerivsRptd

	@NbOfDerivsRptd.setter
	def NbOfDerivsRptd(self, value):
		self._NbOfDerivsRptd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDerivsRptd', Number, False)

	@NbOfDerivsRptd.deleter
	def NbOfDerivsRptd(self):
		del self._NbOfDerivsRptd
		self._NbOfDerivsRptd = base_types.UninitialisedField(self, 'NbOfDerivsRptd', Number, False)

	@property
	def NbOfDerivsRptdWthOtlrs(self):
		return self._NbOfDerivsRptdWthOtlrs

	@NbOfDerivsRptdWthOtlrs.setter
	def NbOfDerivsRptdWthOtlrs(self, value):
		self._NbOfDerivsRptdWthOtlrs = value if value is not None else base_types.UninitialisedField(self, 'NbOfDerivsRptdWthOtlrs', Number, False)

	@NbOfDerivsRptdWthOtlrs.deleter
	def NbOfDerivsRptdWthOtlrs(self):
		del self._NbOfDerivsRptdWthOtlrs
		self._NbOfDerivsRptdWthOtlrs = base_types.UninitialisedField(self, 'NbOfDerivsRptdWthOtlrs', Number, False)

	@property
	def Wrnngs(self):
		return self._Wrnngs

	@Wrnngs.setter
	def Wrnngs(self, value):
		self._Wrnngs = value if value is not None else base_types.UninitialisedField(self, 'Wrnngs', AbnormalValuesData4, True)

	@Wrnngs.deleter
	def Wrnngs(self):
		del self._Wrnngs
		self._Wrnngs = base_types.UninitialisedField(self, 'Wrnngs', AbnormalValuesData4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfDerivsRptd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDerivsRptdWthOtlrs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wrnngs', type=AbnormalValuesData4, min=1, max=None, mutex_group=None, array=True),
	))