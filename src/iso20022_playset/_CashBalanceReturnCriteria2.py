# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class CashBalanceReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_NbOfPmtsInd", "_PrcgDtInd", "_StsInd", "_TpInd", "_ValDtInd"]
	@property
	def NbOfPmtsInd(self):
		return self._NbOfPmtsInd

	@NbOfPmtsInd.setter
	def NbOfPmtsInd(self, value):
		self._NbOfPmtsInd = value if value is not None else base_types.UninitialisedField(self, 'NbOfPmtsInd', RequestedIndicator, False)

	@NbOfPmtsInd.deleter
	def NbOfPmtsInd(self):
		del self._NbOfPmtsInd
		self._NbOfPmtsInd = base_types.UninitialisedField(self, 'NbOfPmtsInd', RequestedIndicator, False)

	@property
	def PrcgDtInd(self):
		return self._PrcgDtInd

	@PrcgDtInd.setter
	def PrcgDtInd(self, value):
		self._PrcgDtInd = value if value is not None else base_types.UninitialisedField(self, 'PrcgDtInd', RequestedIndicator, False)

	@PrcgDtInd.deleter
	def PrcgDtInd(self):
		del self._PrcgDtInd
		self._PrcgDtInd = base_types.UninitialisedField(self, 'PrcgDtInd', RequestedIndicator, False)

	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if value is not None else base_types.UninitialisedField(self, 'StsInd', RequestedIndicator, False)

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = base_types.UninitialisedField(self, 'StsInd', RequestedIndicator, False)

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if value is not None else base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	@property
	def ValDtInd(self):
		return self._ValDtInd

	@ValDtInd.setter
	def ValDtInd(self, value):
		self._ValDtInd = value if value is not None else base_types.UninitialisedField(self, 'ValDtInd', RequestedIndicator, False)

	@ValDtInd.deleter
	def ValDtInd(self):
		del self._ValDtInd
		self._ValDtInd = base_types.UninitialisedField(self, 'ValDtInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfPmtsInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDtInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDtInd', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
	))