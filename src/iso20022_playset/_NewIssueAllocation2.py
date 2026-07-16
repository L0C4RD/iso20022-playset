# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DeMinimus1Choice
from . import Max350Text
from . import YesNoIndicator

class NewIssueAllocation2(base_types._BaseFieldType):

	__slots__ = ["_DeMnms", "_Rstrctd", "_XmptPrsnRsn"]
	@property
	def DeMnms(self):
		return self._DeMnms

	@DeMnms.setter
	def DeMnms(self, value):
		self._DeMnms = value if value is not None else base_types.UninitialisedField(self, 'DeMnms', DeMinimus1Choice, False)

	@DeMnms.deleter
	def DeMnms(self):
		del self._DeMnms
		self._DeMnms = base_types.UninitialisedField(self, 'DeMnms', DeMinimus1Choice, False)

	@property
	def Rstrctd(self):
		return self._Rstrctd

	@Rstrctd.setter
	def Rstrctd(self, value):
		self._Rstrctd = value if value is not None else base_types.UninitialisedField(self, 'Rstrctd', YesNoIndicator, False)

	@Rstrctd.deleter
	def Rstrctd(self):
		del self._Rstrctd
		self._Rstrctd = base_types.UninitialisedField(self, 'Rstrctd', YesNoIndicator, False)

	@property
	def XmptPrsnRsn(self):
		return self._XmptPrsnRsn

	@XmptPrsnRsn.setter
	def XmptPrsnRsn(self, value):
		self._XmptPrsnRsn = value if value is not None else base_types.UninitialisedField(self, 'XmptPrsnRsn', Max350Text, False)

	@XmptPrsnRsn.deleter
	def XmptPrsnRsn(self):
		del self._XmptPrsnRsn
		self._XmptPrsnRsn = base_types.UninitialisedField(self, 'XmptPrsnRsn', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DeMnms', type=DeMinimus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptPrsnRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))