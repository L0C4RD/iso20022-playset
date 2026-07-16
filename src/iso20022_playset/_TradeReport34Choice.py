# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginReportData9

class TradeReport34Choice(base_types._BaseFieldType):

	__slots__ = ["_Crrctn", "_Err", "_MrgnUpd", "_New"]
	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if value is not None else base_types.UninitialisedField(self, 'Crrctn', MarginReportData9, False)

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = base_types.UninitialisedField(self, 'Crrctn', MarginReportData9, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', MarginReportData9, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', MarginReportData9, False)

	@property
	def MrgnUpd(self):
		return self._MrgnUpd

	@MrgnUpd.setter
	def MrgnUpd(self, value):
		self._MrgnUpd = value if value is not None else base_types.UninitialisedField(self, 'MrgnUpd', MarginReportData9, False)

	@MrgnUpd.deleter
	def MrgnUpd(self):
		del self._MrgnUpd
		self._MrgnUpd = base_types.UninitialisedField(self, 'MrgnUpd', MarginReportData9, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', MarginReportData9, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', MarginReportData9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Crrctn', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnUpd', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=MarginReportData9, min=0, max=1, mutex_group=1, array=False),
	))