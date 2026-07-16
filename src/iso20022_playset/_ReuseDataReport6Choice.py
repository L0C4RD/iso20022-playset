# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReuseDataReportCorrection14
from . import ReuseDataReportError5
from . import ReuseDataReportNew6

class ReuseDataReport6Choice(base_types._BaseFieldType):

	__slots__ = ["_CollReuseUpd", "_Crrctn", "_Err", "_New"]
	@property
	def CollReuseUpd(self):
		return self._CollReuseUpd

	@CollReuseUpd.setter
	def CollReuseUpd(self, value):
		self._CollReuseUpd = value if value is not None else base_types.UninitialisedField(self, 'CollReuseUpd', ReuseDataReportCorrection14, False)

	@CollReuseUpd.deleter
	def CollReuseUpd(self):
		del self._CollReuseUpd
		self._CollReuseUpd = base_types.UninitialisedField(self, 'CollReuseUpd', ReuseDataReportCorrection14, False)

	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if value is not None else base_types.UninitialisedField(self, 'Crrctn', ReuseDataReportCorrection14, False)

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = base_types.UninitialisedField(self, 'Crrctn', ReuseDataReportCorrection14, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', ReuseDataReportError5, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', ReuseDataReportError5, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', ReuseDataReportNew6, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', ReuseDataReportNew6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollReuseUpd', type=ReuseDataReportCorrection14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Crrctn', type=ReuseDataReportCorrection14, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=ReuseDataReportError5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=ReuseDataReportNew6, min=0, max=1, mutex_group=1, array=False),
	))