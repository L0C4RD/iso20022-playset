# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max350Text import Max350Text

class DeMinimusNotApplicable1(base_types._BaseFieldType):

	__slots__ = ["_RstrctdPrsnRsn"]
	@property
	def RstrctdPrsnRsn(self):
		return self._RstrctdPrsnRsn

	@RstrctdPrsnRsn.setter
	def RstrctdPrsnRsn(self, value):
		self._RstrctdPrsnRsn = value if type(value) != base_types.auto else self.make_default("RstrctdPrsnRsn")

	@RstrctdPrsnRsn.deleter
	def RstrctdPrsnRsn(self):
		del self._RstrctdPrsnRsn
		self._RstrctdPrsnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RstrctdPrsnRsn', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))