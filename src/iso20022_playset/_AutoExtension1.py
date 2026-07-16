# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AutoExtend1Choice
from . import ISODate
from . import NonExtension1

class AutoExtension1(base_types._BaseFieldType):

	__slots__ = ["_FnlXpryDt", "_NonXtnsnNtfctn", "_Prd"]
	@property
	def FnlXpryDt(self):
		return self._FnlXpryDt

	@FnlXpryDt.setter
	def FnlXpryDt(self, value):
		self._FnlXpryDt = value if value is not None else base_types.UninitialisedField(self, 'FnlXpryDt', ISODate, False)

	@FnlXpryDt.deleter
	def FnlXpryDt(self):
		del self._FnlXpryDt
		self._FnlXpryDt = base_types.UninitialisedField(self, 'FnlXpryDt', ISODate, False)

	@property
	def NonXtnsnNtfctn(self):
		return self._NonXtnsnNtfctn

	@NonXtnsnNtfctn.setter
	def NonXtnsnNtfctn(self, value):
		self._NonXtnsnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'NonXtnsnNtfctn', NonExtension1, True)

	@NonXtnsnNtfctn.deleter
	def NonXtnsnNtfctn(self):
		del self._NonXtnsnNtfctn
		self._NonXtnsnNtfctn = base_types.UninitialisedField(self, 'NonXtnsnNtfctn', NonExtension1, True)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', AutoExtend1Choice, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', AutoExtend1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FnlXpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonXtnsnNtfctn', type=NonExtension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prd', type=AutoExtend1Choice, min=0, max=1, mutex_group=None, array=False),
	))